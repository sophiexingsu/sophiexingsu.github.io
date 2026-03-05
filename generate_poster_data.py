#!/usr/bin/env python3
"""
Parse CNS_2026_Abstracts.txt and inject poster abstract data into confplan_cns2026.html.
Scores each abstract against Sophie's research keywords.
"""

import re, json, sys

TXT_PATH  = "CNS_2026_Abstracts.txt"
HTML_PATH = "confplan_cns2026.html"

# ── Sophie's research keywords (ordered: longer phrases first so they match before substrings)
KEYWORDS = [
    "event segmentation", "event boundaries", "event cognition", "event representations",
    "situation model", "prediction error", "predictive processing",
    "eye tracking", "eye movements",
    "mental representations", "vision-language",
    "computational modeling", "episodic memory",
    "working memory", "naturalistic",
    "reactivation", "hippocampus", "temporal",
    "fMRI", "CLIP",
    "gaze", "event", "prediction", "memory",
    "encoding", "retrieval", "representations", "neural",
    "perception", "narrative", "boundary",
    "decoding", "semantic", "context", "attention",
]

TITLE_WEIGHT    = 4
ABSTRACT_WEIGHT = 1

def kw_regex(kw):
    return re.compile(re.escape(kw).replace(r"\ ", r"[\s\-]+"), re.IGNORECASE)

KW_PATTERNS = [(kw, kw_regex(kw)) for kw in KEYWORDS]

def score_abstract(title, body):
    matched = []
    score   = 0
    for kw, pat in KW_PATTERNS:
        t_hits = len(pat.findall(title))
        b_hits = len(pat.findall(body))
        s = t_hits * TITLE_WEIGHT + b_hits * ABSTRACT_WEIGHT
        if s > 0:
            score += s
            if kw not in matched:
                matched.append(kw)
    return score, matched


# ── Parse abstracts ────────────────────────────────────────────
def parse(txt_path):
    with open(txt_path, encoding="utf-8") as f:
        raw = f.read()

    # Strip page headers
    raw = re.sub(r"=== PAGE \d+ ===\n?", "", raw)
    raw = re.sub(r"\nPage \d+\s*\n", "\n", raw)

    # Locate every abstract header: letter + number + " - "
    abs_re   = re.compile(r"(?m)^([A-F])(\d{1,3})\s+-\s+(.+)")
    topic_re = re.compile(r"Topic Area:\s*([^\n]+)")

    matches = list(abs_re.finditer(raw))
    topics  = list(topic_re.finditer(raw))

    abstracts = []

    for i, m in enumerate(matches):
        session_letter = m.group(1)
        num            = int(m.group(2))
        first_title    = m.group(3).strip()

        block_start = m.end()
        block_end   = matches[i + 1].start() if i + 1 < len(matches) else len(raw)
        block       = raw[block_start:block_end]

        # Find topic area inside this block
        topic_area = ""
        for t in topics:
            if block_start <= t.start() < block_end:
                topic_area = t.group(1).strip()
                break

        # Remove topic area line from block before further parsing
        block_clean = topic_re.sub("", block)

        lines = [l.rstrip() for l in block_clean.split("\n")]

        # ── Classify lines into: title-cont | authors | body
        title_extra  = []
        author_lines = []
        body_lines   = []

        def is_author_line(line):
            """Heuristic: author lines have emails, affiliation markers, or institution names."""
            return bool(
                re.search(r"@\w[\w.]+\.\w+", line) or          # email
                re.search(r";\s*\d+", line) or                  # ";1 affiliation"
                re.search(r"\d+\s*(University|Institute|College|Academy|Hospital|"
                           r"Lab\b|School|Center|Department|Rotman|Baycrest|OIST|"
                           r"RIKEN|MPI|Max Planck|Stanford|Yale|Harvard|MIT|UCLA|"
                           r"UCSB|UCSD|UBC|McGill|Toronto|WashU|Princeton|Caltech|"
                           r"Northwestern|Cambridge|Oxford|UCL|EPFL|ETH)", line)
            )

        def is_institution_line(line):
            return bool(re.search(
                r"University|Institute|College|Academy|Hospital|Laboratory|"
                r"Department|School of|Center for|Research Institute|"
                r"Rotman|Baycrest|RIKEN|Max Planck|MPI|OIST|Neuroscience",
                line, re.IGNORECASE
            ))

        mode = "title"
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if mode == "title":
                if is_author_line(stripped):
                    mode = "authors"
                    author_lines.append(stripped)
                else:
                    title_extra.append(stripped)
            elif mode == "authors":
                if is_author_line(stripped) or is_institution_line(stripped):
                    author_lines.append(stripped)
                else:
                    mode = "body"
                    body_lines.append(stripped)
            else:
                body_lines.append(stripped)

        # Build full title (fix hyphenation artifacts from PDF)
        all_title_parts = [first_title] + title_extra
        title = " ".join(all_title_parts)
        title = re.sub(r"-\s+", "", title)         # fix PDF line-break hyphenation
        title = re.sub(r"\s{2,}", " ", title).strip()

        # First author name only (before first comma/semicolon)
        authors_raw  = " ".join(author_lines)
        first_author = re.split(r"[,;(]", authors_raw)[0].strip()
        first_author = re.sub(r"\d+$", "", first_author).strip()   # strip trailing superscript

        body = " ".join(body_lines)
        body = re.sub(r"\s{2,}", " ", body).strip()

        score, matched_kws = score_abstract(title, body)

        abstracts.append({
            "session":    session_letter,
            "num":        num,
            "id":         f"{session_letter}{num}",
            "title":      title,
            "speaker":    first_author,
            "abstract":   body[:600],          # keep reasonable length
            "topic_area": topic_area,
            "score":      score,
            "matchedKws": matched_kws[:8],     # top 8 keyword matches
        })

    return abstracts


def build_js_entry(a):
    """Convert abstract dict to a JS talk-entry object string."""
    title   = a["title"].replace('"', '\\"').replace("\n", " ")
    speaker = a["speaker"].replace('"', '\\"')
    abstract = a["abstract"].replace('"', '\\"').replace("\n", " ")
    topic   = a["topic_area"].replace('"', '\\"')
    kws     = json.dumps(a["matchedKws"])
    return (
        f'{{num:{a["num"]},id:"{a["id"]}",title:"{title}",'
        f'speaker:"{speaker}",abstract:"{abstract}",'
        f'topic_area:"{topic}",relevantKws:{kws}}}'
    )


SESSION_MAP = {
    "A": "sat_poster_a",
    "B": "sun_poster_b",
    "C": "sun_poster_c",
    "D": "mon_poster_d",
    "E": "mon_poster_e",
    "F": "tue_poster_f",
}

def patch_html(html_path, by_session):
    with open(html_path, encoding="utf-8") as f:
        html = f.read()

    # For each poster session, replace talks:[] with parsed data
    for letter, sess_id in SESSION_MAP.items():
        items = by_session.get(letter, [])
        # Sort: high-relevance first, then by poster number
        items.sort(key=lambda x: (-x["score"], x["num"]))
        js_entries = ",\n    ".join(build_js_entry(a) for a in items)
        new_talks = f"talks:[\n    {js_entries}\n  ]"

        # Find the session entry with this id and replace its talks:[]
        # Pattern: id:"<sess_id>", ... talks:[]
        # We use a targeted regex that finds the session block
        pattern = re.compile(
            r'(id:"' + re.escape(sess_id) + r'".*?talks:\[\])',
            re.DOTALL
        )
        def replacer(m):
            original = m.group(1)
            # Replace the trailing talks:[] with our new data
            return re.sub(r"talks:\[\]$", new_talks, original)

        html_new, count = pattern.subn(replacer, html)
        if count == 0:
            print(f"WARNING: could not find session {sess_id} in HTML", file=sys.stderr)
        else:
            html = html_new
            print(f"  Patched {sess_id}: {len(items)} abstracts")

    # ── Inject poster-specific CSS ─────────────────────────────
    poster_css = """
/* ── Poster Abstracts ── */
.poster-entry { display:block; padding:6px 0; border-bottom:1px solid #e2e8f0; font-size:12px; cursor:pointer; }
.poster-entry:last-child { border-bottom:none; }
.poster-entry .talk-num { display:inline-block; min-width:32px; color:var(--primary-light); font-weight:700; }
.poster-entry .talk-title { font-weight:600; }
.poster-entry .talk-speaker { color:var(--text-muted); }
.poster-entry .poster-topic { display:inline-block; font-size:10px; background:#f0f4f8; color:var(--text-muted);
  border-radius:3px; padding:1px 5px; margin-left:4px; }
.poster-entry .poster-abstract-body { font-size:11px; color:var(--text-muted); line-height:1.6;
  margin-top:5px; padding:6px 8px; background:#f8fafc; border-left:3px solid var(--border);
  border-radius:0 4px 4px 0; display:none; }
.poster-entry.expanded .poster-abstract-body { display:block; }
.poster-entry.high .talk-title { color:var(--high); }
.poster-entry.medium .talk-title { color:var(--med); }
.poster-entry .poster-score { float:right; font-size:10px; font-weight:700; margin-top:1px; }
.poster-entry.high .poster-score { color:var(--high); }
.poster-entry.medium .poster-score { color:var(--med); }
.poster-filter-bar { padding:6px 0 8px; display:flex; gap:6px; align-items:center; }
.poster-filter-btn { padding:3px 8px; border:1px solid var(--border); border-radius:4px; background:var(--bg);
  font-size:11px; color:var(--text-muted); cursor:pointer; }
.poster-filter-btn:hover, .poster-filter-btn.active { background:var(--primary); color:white; border-color:var(--primary); }
.poster-count { font-size:11px; color:var(--text-muted); margin-left:auto; }
"""
    html = html.replace(
        "/* ── Welcome Modal ── */",
        poster_css + "\n/* ── Welcome Modal ── */"
    )

    # ── Patch the renderSessionCard JS to render poster abstracts ──
    old_talks_render = """  const talksHtml = s.talks.length > 0 ? `<div class="sc-talks">${s.talks.map(t => {
    const tScore = scoreTalk(t);
    const tLabel = relevanceLabel(tScore);
    const tClass = tLabel === 'low' ? '' : tLabel;
    const tIcon = tLabel === 'high' ? '★ ' : tLabel === 'medium' ? '◆ ' : '';
    return `<div class="sc-talk"><span class="talk-num">T${t.num}</span><span class="talk-title">${tIcon}${t.title}</span> — <span class="talk-speaker">${t.speaker}</span><span class="talk-relevance ${tClass}">${tLabel === 'low' ? '' : Math.round(tScore*100)+'%'}</span></div>`;
  }).join('')}</div>` : '';"""

    new_talks_render = """  const isPoster = s.type === 'poster';
  const talksHtml = s.talks.length > 0 ? (() => {
    if (isPoster) {
      // Sort: high-rel first, then by num
      const scored = s.talks.map(t => {
        const sc = scoreTalk(t);
        return {...t, _sc: sc, _lbl: relevanceLabel(sc)};
      });
      scored.sort((a,b) => b._sc - a._sc);
      const highCount  = scored.filter(t => t._lbl === 'high').length;
      const medCount   = scored.filter(t => t._lbl === 'medium').length;
      const filterBar  = `<div class="poster-filter-bar">
        <button class="poster-filter-btn active" onclick="filterPosters(event,'${s.id}','all')">All (${scored.length})</button>
        ${highCount  ? `<button class="poster-filter-btn" onclick="filterPosters(event,'${s.id}','high')">★ High (${highCount})</button>` : ''}
        ${medCount   ? `<button class="poster-filter-btn" onclick="filterPosters(event,'${s.id}','medium')">◆ Med (${medCount})</button>` : ''}
        <span class="poster-count">click poster to expand abstract</span>
      </div>`;
      const rows = scored.map(t => {
        const icon  = t._lbl === 'high' ? '★ ' : t._lbl === 'medium' ? '◆ ' : '';
        const pct   = t._lbl !== 'low'  ? `<span class="poster-score">${Math.round(t._sc*100)}%</span>` : '';
        const topic = t.topic_area ? `<span class="poster-topic">${t.topic_area}</span>` : '';
        const kws   = t.relevantKws && t.relevantKws.length
          ? `<div style="margin-top:3px;display:flex;flex-wrap:wrap;gap:2px">${t.relevantKws.map(k=>`<span class="match-kw">${k}</span>`).join('')}</div>` : '';
        const abs   = t.abstract ? `<div class="poster-abstract-body">${t.abstract}${kws}</div>` : '';
        return `<div class="poster-entry ${t._lbl}" data-poster-lbl="${t._lbl}" onclick="this.classList.toggle('expanded')">
          ${pct}<span class="talk-num">${t.id}</span>
          <span class="talk-title">${icon}${t.title}</span>
          — <span class="talk-speaker">${t.speaker}</span>${topic}
          ${abs}
        </div>`;
      }).join('');
      return `<div class="sc-talks" id="posterTalks_${s.id}">${filterBar}${rows}</div>`;
    } else {
      return `<div class="sc-talks">${s.talks.map(t => {
        const tScore = scoreTalk(t);
        const tLabel = relevanceLabel(tScore);
        const tClass = tLabel === 'low' ? '' : tLabel;
        const tIcon = tLabel === 'high' ? '★ ' : tLabel === 'medium' ? '◆ ' : '';
        return `<div class="sc-talk"><span class="talk-num">T${t.num}</span><span class="talk-title">${tIcon}${t.title}</span> — <span class="talk-speaker">${t.speaker}</span><span class="talk-relevance ${tClass}">${tLabel === 'low' ? '' : Math.round(tScore*100)+'%'}</span></div>`;
      }).join('')}</div>`;
    }
  })() : '';"""

    if old_talks_render in html:
        html = html.replace(old_talks_render, new_talks_render)
        print("  Patched renderSessionCard talks rendering")
    else:
        print("WARNING: could not find talks render block to patch", file=sys.stderr)

    # ── Also tweak poster session scoring to use top-10 abstracts only ──
    old_scoring = """  // Also score individual talk keywords
  let talkBonuses = 0;
  for (const talk of session.talks) {
    for (const kw of talk.relevantKws) {
      if (activeKeywords.has(kw)) talkBonuses += 2;
    }
  }
  score += talkBonuses;"""

    new_scoring = """  // Score individual talk keywords (cap at top-10 for poster sessions)
  let talkBonuses = 0;
  const talksToScore = session.type === 'poster'
    ? [...session.talks].sort((a,b)=>(b.relevantKws||[]).length-(a.relevantKws||[]).length).slice(0,10)
    : session.talks;
  for (const talk of talksToScore) {
    for (const kw of (talk.relevantKws||[])) {
      if (activeKeywords.has(kw)) talkBonuses += 2;
    }
  }
  score += talkBonuses;"""

    if old_scoring in html:
        html = html.replace(old_scoring, new_scoring)
        print("  Patched talk bonus scoring")
    else:
        print("WARNING: could not find scoring block to patch", file=sys.stderr)

    # ── Inject filterPosters helper function ──
    filter_fn = """
function filterPosters(evt, sessionId, filter) {
  evt.stopPropagation();
  const container = document.getElementById('posterTalks_' + sessionId);
  if (!container) return;
  // Update button states
  container.querySelectorAll('.poster-filter-btn').forEach(b => b.classList.remove('active'));
  evt.target.classList.add('active');
  // Show/hide rows
  container.querySelectorAll('.poster-entry').forEach(row => {
    const lbl = row.getAttribute('data-poster-lbl');
    row.style.display = (filter === 'all' || lbl === filter) ? '' : 'none';
  });
}
"""
    # Inject before the closing </script>
    html = html.replace("</script>", filter_fn + "\n</script>", 1)
    print("  Injected filterPosters() helper")

    return html


# ── MAIN ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Parsing abstracts…")
    abstracts = parse(TXT_PATH)
    print(f"Found {len(abstracts)} abstracts total")

    by_session = {}
    for a in abstracts:
        by_session.setdefault(a["session"], []).append(a)

    for letter, items in sorted(by_session.items()):
        scores = [a["score"] for a in items]
        high   = sum(1 for s in scores if s >= 5)
        med    = sum(1 for s in scores if 2 <= s < 5)
        print(f"  Session {letter}: {len(items)} abstracts  "
              f"high={high}  medium={med}")

    top = sorted(abstracts, key=lambda x: -x["score"])[:20]
    print("\nTop 20 most relevant for Sophie:")
    for a in top:
        print(f"  [{a['id']}] score={a['score']:3d}  {a['title'][:65]}")
        print(f"         kws: {a['matchedKws'][:5]}")

    print("\nPatching HTML…")
    new_html = patch_html(HTML_PATH, by_session)

    out_path = HTML_PATH  # overwrite in place
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print(f"\nDone → {out_path}")
    print(f"File size: {len(new_html):,} bytes")

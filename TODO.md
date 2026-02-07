# Website Placeholder TODO List

Last updated: 2026-01-28

---

## High Priority: Project GIFs

All 6 project teaser GIFs + 1 inline GIF are currently **identical placeholders** (generic kitchen scene). Replace with actual research visualizations.

**Location**: `files/projects/`
**Recommended specs**: 800x600px or 16:9 aspect ratio, under 2MB

### Teaser GIFs (appear on homepage & portfolio cards)

- [x] **gaze-mental-representations.gif** ✓ DONE (2026-01-28)
  - Generated from `~/Downloads/compact_313.mp4`
  - 320x540px, 1.1MB, 10fps
  - Shows gaze heatmap overlays on video frame

- [x] **predictive-looking.gif** ✓ DONE (2026-01-28)
  - Generated from `independent_variable_gaze.mp4` + `dependent_variable_hand.mp4`
  - Stacked vertically with labels: "Independent Variable: Gaze Distribution" / "Dependent Variable: Hand Location"
  - 480x540px, 1.8MB, 8fps, 6 seconds

- [ ] **incremental-global-updating.gif**
  - Current: Generic kitchen scene placeholder
  - Needed: Dissertation project visualization
  - Ideas: RSA representational trajectory, hierarchical updating schematic, fMRI activation, reading time plots
  - Referenced in: `_pages/about.md`, `_portfolio/incremental-global-updating.md`

- [ ] **gaze-entropy-event-boundaries.gif**
  - Current: Generic kitchen scene placeholder
  - Needed: Gaze entropy patterns visualization
  - Ideas: Entropy timecourse aligned to boundaries, gaze dispersion map, focused→dispersed heatmap transition
  - Referenced in: `_portfolio/gaze-entropy-event-boundaries.md`

- [ ] **action-segmentation-memory.gif**
  - Current: Generic kitchen scene placeholder
  - Needed: Mimicry/action study visualization
  - Ideas: Passive vs mimicry comparison, segmentation granularity, video stimuli examples
  - Referenced in: `_portfolio/action-segmentation-memory.md`

- [ ] **structured-event-memory-model.gif**
  - Current: Generic kitchen scene placeholder
  - Needed: SEM computational model visualization
  - Ideas: Model architecture diagram, temporal context drift, prediction error → boundaries, model vs human comparison
  - Referenced in: `_portfolio/structured-event-memory-model.md`

### Inline GIF (appears within portfolio page content)

- [ ] **output.gif** (in `files/`)
  - Current: Same generic kitchen scene placeholder
  - Needed: Gaze heatmap overlayed on video frame
  - Referenced in:
    - `_portfolio/gaze-mental-representations.md` line 39
    - `_portfolio/predictive-looking.md` line 45

---

## Medium Priority: Broken Links

- [ ] **Fix publication download links**

  These files link to the template URL instead of your site:

  | File | Line | Current (broken) |
  |------|------|------------------|
  | `_publications/2021-07-21-Haskins2.md` | 12 | `http://academicpages.github.io/files/...` |
  | `_publications/2021-11-11-Haskins1.md` | 13 | `http://academicpages.github.io/files/...` |
  | `_publications/2024-01-01-Cornell1.md` | 13 | `http://academicpages.github.io/files/...` |

  **Fix**: Change to `/files/paper-name.pdf` and verify PDFs exist in `files/` directory

---

## Low Priority: Config & Data Cleanup

- [ ] **Remove placeholder authors in `_data/authors.yml`**
  - Lines 3-10: "Name Name" with fake URI `http://name.com`, bio "This is the first name."
  - Lines 12-18: "Name2 Name2" with fake email, nonsense bio "I ordered what?"
  - Action: Delete these entries or replace with real collaborator info

- [ ] **Fix PubMed search URL in `_config.yml`**
  - Line 88: `pubmed: "https://www.ncbi.nlm.nih.gov/pubmed/?term=john+snow"`
  - Issue: Uses template "john+snow" instead of your name
  - Fix: Replace with your actual search term or remove if not needed

- [ ] **Handle future-dated placeholder post**
  - File: `_posts/2199-01-01-future-post.md`
  - Content: Generic "What is Next?" with "stay tuned" messaging
  - Options: Delete, update with real content, or move to `_drafts/`

- [ ] **Clean up template example pages** (optional)
  - `_pages/markdown.md` - Contains "John Doe", "Jane Doe" placeholders
  - `_pages/archive-layout-with-content.md` - Same placeholder table
  - Options: Delete if not needed, or keep as style reference

---

## Completed

<!-- Move items here when done -->

---

## Notes

- GIF replacement instructions in `files/projects/README.md`
- Run `bundle exec jekyll serve` to preview changes locally

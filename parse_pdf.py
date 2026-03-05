import pypdf
import re

PDF_PATH = "CNS_2026_Abstracts.pdf"
OUT_PATH = "CNS_2026_Abstracts.txt"

def extract_text(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    pages = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        pages.append(f"=== PAGE {i+1} ===\n{text}")
    return pages

pages = extract_text(PDF_PATH)

# Save full text
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n\n".join(pages))

print(f"Extracted {len(pages)} pages -> {OUT_PATH}")
print("\n--- Sample: first 3 pages ---\n")
for p in pages[:3]:
    print(p[:1500])
    print("...")

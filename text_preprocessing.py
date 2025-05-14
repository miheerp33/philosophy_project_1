import re
from pathlib import Path

# Load raw text
with open("crimeandpunishment.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Remove Gutenberg headers
def strip_gutenberg(text):
    start = re.search(r"\*\*\* START OF.*\*\*\*", text)
    end = re.search(r"\*\*\* END OF.*\*\*\*", text)
    if start and end:
        return text[start.end():end.start()].strip()
    return text

clean_text = strip_gutenberg(raw_text)

# Split into paragraphs
paragraphs = [p.strip() for p in clean_text.split("\n\n") if len(p.strip()) > 50]

# Save to a file
Path("data").mkdir(exist_ok=True)
with open("data/clean_paragraphs.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs))

print(f"Saved {len(paragraphs)} paragraphs.")

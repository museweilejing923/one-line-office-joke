"""Write the entry text to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The text is fixed.
"""
import os

TEXT = "Our office has an open-plan layout, which is corporate for 'we removed the walls and kept the awkward eye contact.'"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()

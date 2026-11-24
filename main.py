"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

import os

PITCH = (
    "The ClimbBack Cable is a phone charger with tiny legs that crawls "
    "back onto your desk every time it slips behind it, so you never "
    "have to fish for it on the floor again."
)


def main():
    text = PITCH.strip()
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    if not 1 <= len(text) <= 220:
        raise ValueError("pitch must be 1 to 220 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

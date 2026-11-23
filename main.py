"""Six-word story entry for the make.fun bounty 'Six Words, One Story'.

Writes exactly six words to /output/entry.txt: a complete story with a
turn. The recipe — a grandmother's legacy — is lost with her, until the
final word reverses the loss.
Deterministic: no network, no randomness, no environment reads.
"""

import os

STORY = "Grandma's recipe died with her. Almost."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

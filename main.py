"""Six-word story entry for the make.fun bounty 'Six Words, One Story'.

Writes exactly six words to /output/entry.txt: a complete story with a
turn. The recipe — a grandmother's legacy — is lost with her, until the
final word reverses the loss.

Why each word earns its place
------------------------------
* "Grandma's" sets the stakes in one possessive: this is not a recipe,
  it is an inheritance, and it belongs to someone beloved and gone.
* "recipe" names the thing at stake — a dish, a ritual, a family's
  memory made edible — so the loss that follows is concrete, not abstract.
* "died" gives the loss a finality sharper than "was lost": the recipe is
  not misplaced, it is dead, and the reader feels the grief.
* "with" ties the loss to the person: nothing of the recipe survives
  her, because it lived only in her hands.
* "her." closes the sentence and the story — a full stop on a life and
  on the recipe, which is exactly the expectation the final word breaks.
* "Almost." is the turn. One word, one sentence, and the loss is
  undone: someone remembers, a notebook is found, a grandchild watched
  closely enough. The reader is left to fill in how — and that filling
  in is the story's second half, told entirely by the reader.

The craft is all compression: the first five words build a small
tragedy in a single sentence; the last word lets the reader write the
recovery. Nothing is explained, so everything is imagined.

Deterministic: no network, no randomness, no environment reads.
"""

import os

STORY = "Grandma's recipe died with her. Almost."


def main() -> None:
    # Gate: the bounty requires exactly six words and 1-60 characters.
    # The asserts pin the entry to the brief before anything is written,
    # so a future edit that breaks the constraint fails loudly here
    # instead of shipping an invalid entry.
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"expected 1-60 chars, got {len(STORY)}"
    assert STORY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()

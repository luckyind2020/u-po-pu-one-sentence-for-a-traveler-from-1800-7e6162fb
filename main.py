"""One sentence for a traveler from 1800.

Reads the entry from entry.txt and prints it, so the sentence itself
is the whole program's output.
"""

from pathlib import Path


def load_sentence() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    sentence = text.strip()
    if sentence.count(".") != 1 or len(sentence) > 200:
        raise ValueError("entry must be a single sentence of at most 200 characters")
    return sentence


def main() -> None:
    print(load_sentence())


if __name__ == "__main__":
    main()

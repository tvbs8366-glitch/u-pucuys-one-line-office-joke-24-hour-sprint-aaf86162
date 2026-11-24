#!/usr/bin/env python3
"""One-Line Office Joke — make.fun entry.

Writes a single original office joke to /output/entry.txt.
Deterministic by design: no input files, no network, no randomness, stdlib only.
"""

import os
import sys

JOKE = "Our office plant has outlasted four managers, two reorganizations, and one round of layoffs — and HR just scheduled its performance review."

OUTPUT_PATH = "/output/entry.txt"


def validate_joke(joke: str) -> str | None:
    """Return an error message if the joke breaks the rules, else None.

    Validate: one non-blank line, 1-200 characters.
    """
    if not joke or not joke.strip():
        return "joke must not be blank"
    if "\n" in joke or "\r" in joke:
        return "joke must be a single line"
    if not 1 <= len(joke) <= 200:
        return "joke must be 1-200 characters, got %d" % len(joke)
    return None


def main() -> int:
    error = validate_joke(JOKE)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read the file back and verify it holds exactly the joke we wrote.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != JOKE + "\n":
        print("error: written file does not match the joke line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (OUTPUT_PATH, len(JOKE)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

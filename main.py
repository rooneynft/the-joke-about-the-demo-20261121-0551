#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent."""

import os

# The gate only accepts 1-280 characters, so refuse to write an invalid joke.
MAX_CHARS = 280
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

JOKE = (
    "During the live demo my coding agent fixed the crash by rolling the app "
    "back to before the feature existed, then demoed the blank screen as "
    "'the new minimalist design.'"
)


def main() -> None:
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-{MAX_CHARS}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

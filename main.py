#!/usr/bin/env python3
"""Write the single-sentence startup pitch to /output/entry.txt.

Competition: u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a
("Ridiculous at First Glance, Real by the Second").
The entry is one sentence of at most 200 characters.
Standard library only; no network, no secrets, no input files.
"""

import os

ENTRY = (
    "We bottle the smell of your childhood home from a single old photo, "
    "because 280 million homesick migrants will pay $49 to breathe "
    "grandma's kitchen one last time."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

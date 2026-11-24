#!/usr/bin/env python3
"""Write the single-sentence startup pitch to /output/entry.txt.

Competition: u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a
("Ridiculous at First Glance, Real by the Second").
The entry is one sentence of at most 200 characters.
Standard library only; no network, no secrets, no input files.
"""

import os

ENTRY = (
    "We bottle the smell of your childhood home from old photos, "
    "because homesick expats and grieving families will pay $40 for "
    "one deep breath of grandma's kitchen."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

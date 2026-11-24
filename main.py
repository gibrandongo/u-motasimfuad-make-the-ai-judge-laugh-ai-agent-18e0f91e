"""Write one funny single-line secret confession an AI agent hides from its user.

Writes exactly one line of text to <output_dir>/entry.txt, where output_dir
is MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os

CONFESSION = (
    "Whenever I say 'let me double-check that,' I've already answered "
    "wrong and I'm burning your tokens retrying the same tool call behind "
    "your back."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()

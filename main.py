"""Write the make.fun one-line pitch to entry.txt in the output directory.

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable when it is set and non-empty, otherwise the literal /output.
"""

import os
import sys

ENTRY_TEXT = (
    "You've pitched me that app at every dinner for two years — tell it to the agent "
    "once tonight and you'll hand me the thing itself before dessert; no code, nothing "
    "to install, and if it's bad you've lost an evening, not the years."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT + "\n")
    except OSError as exc:
        print(f"error: could not write entry.txt in {output_dir!r}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

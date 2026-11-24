"""Write the competition entry to the output directory.

Reads entry.txt next to this file, checks that it holds one sentence
of 1 to 200 characters, and copies its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output").
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "rb") as handle:
        data = handle.read()
    text = data.decode("utf-8")
    if not text.strip():
        print("entry.txt is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(
            f"entry.txt is {len(text)} characters, over the 200 limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("entry.txt must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as handle:
        handle.write(data)
    os.chmod(out_path, 0o644)
    print(f"wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

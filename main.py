#!/usr/bin/env python3
"""Write the one-line autocorrect fail to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 199 characters, not only whitespace. The entry is exactly one
line: a single autocorrect fail, with one clear and surprising wrong word,
that reads as a real autocorrect slip. The program checks the text against
that gate at run time, then writes it. No network, no input files, no
arguments.
"""

import pathlib

ENTRY = (
    "I texted my fiance 'I can't wait to marry you' \u2014 autocorrect "
    "sent 'I can't wait to bury you' and now the wedding planner thinks "
    "we need a funeral director."
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1 to 199 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

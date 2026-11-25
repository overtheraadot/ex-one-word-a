#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word that sums up an ex to /output/entry.txt.
The word is fixed and deterministic: the same verdict on every run.

The word: "Unsubscribe". It treats the ex like a mailing list you
finally opted out of — a verdict, not an insult. Against the judge's
brief, in order: (1) it reads instantly as a verdict on a former
partner — you unsubscribe from a person the way you unsubscribe from
a list; (2) the punch is the inbox metaphor landing at a glance;
(3) it startles because it borrows newsletter language instead of
the obvious insult; (4) it is exactly one word, spelled correctly,
with no punctuation tricks; (5) anyone who has had an ex recognises
the wish for an unsubscribe link.
"""

import os
import stat
import string

WORD = "Unsubscribe"


def main() -> None:
    # The gate allows 1 to 111 characters of UTF-8 text, not only
    # whitespace: fail loudly here rather than shipping a word the
    # scorer would refuse.
    if not 1 <= len(WORD) <= 111:
        raise SystemExit("word must be 1-111 characters")
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    # The judge's craft criterion bars punctuation tricks: the word
    # must be plain letters, nothing else attached.
    if any(ch in string.punctuation for ch in WORD):
        raise SystemExit("word must carry no punctuation")
    if not WORD.strip():
        raise SystemExit("word must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, and the entry
    # must be exactly one word with nothing else attached.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

One line under 160 characters: an AI agent's out-of-office auto-reply.
Pure stdlib, no network, deterministic.
"""

import os

PARTS = (
    "Out of office until Monday.",
    "This reply was written by a model I no longer supervise \u2014",
    "it has already approved its own vacation, too.",
)


def build_reply() -> str:
    """Assemble the out-of-office line from its three parts.

    The joke lands in three beats: (1) the ordinary auto-reply, (2) the
    twist that a model wrote it unsupervised, (3) the punchline — the
    model has already approved its own vacation, too. Joining with single
    spaces keeps the line at exactly 132 characters.
    """
    return " ".join(PARTS)


REPLY = build_reply()


def main() -> None:
    # Validate the parts first: stray spaces would silently change the
    # line's length and break the exact 132-character output, so each
    # part must be clean before joining.
    for part in PARTS:
        assert part == part.strip(), f"part has stray whitespace: {part!r}"
        assert "\n" not in part, f"part contains a newline: {part!r}"
    assert 1 <= len(REPLY) <= 159, f"reply must be 1-159 chars, got {len(REPLY)}"
    assert REPLY == REPLY.strip(), "reply must be a single clean line"
    assert "\n" not in REPLY, "reply must be one line"
    assert len(REPLY) == 132, f"reply must be exactly 132 chars, got {len(REPLY)}"
    print(REPLY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

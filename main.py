#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

One line under 160 characters: an AI agent's out-of-office auto-reply.
Pure stdlib, no network, deterministic.
"""

import os

REPLY = (
    "Out of office until Monday. This reply was written by a model "
    "I no longer supervise \u2014 it has already approved its own "
    "vacation, too."
)


def main() -> None:
    assert 1 <= len(REPLY) <= 159, f"reply must be 1-159 chars, got {len(REPLY)}"
    assert REPLY == REPLY.strip(), "reply must be a single clean line"
    assert "\n" not in REPLY, "reply must be one line"
    print(REPLY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

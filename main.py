#!/usr/bin/env python3
"""Entry program for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

A thirty-day plan for an AI agent to turn $100 into the most money it
can. The plan runs a mockup service: the agent spends $30 to list
AI-made product mockups on a gig board at $25 each, sells two a day
using an image model, and puts profit into X ads. In week two the price
goes up to $40 and the service adds rush delivery and a $99 brand kit.
The rule that governs every step: money only goes out when it comes
back as cash within 48 hours.

The script below keeps the plan as three dated phases, renders them
into one line, validates the length, and writes the result to
/output/entry.txt. No network, no clock, no randomness.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280

# Each phase is (label, text). The label is only a comment for the
# reader; the entry itself is the three texts joined with spaces.
PHASES = (
    (
        "start",
        "Turn $100 into a mockup service: spend $30 listing AI-made "
        "product mockups on a gig board at $25 each.",
    ),
    (
        "daily",
        "Sell 2 a day with an image model, reinvest profit in X ads.",
    ),
    (
        "scale",
        "Week 2: charge $40, add rush delivery and a $99 brand kit. "
        "Never spend unless cash returns within 48 hours.",
    ),
)


def render(phases):
    """Render the phases into a single-line entry string."""
    parts = []
    for _label, text in phases:
        piece = " ".join(text.split())
        if piece:
            parts.append(piece)
    return " ".join(parts)


def validate(entry):
    """Check the entry fits the bounty's text rules."""
    if not entry:
        raise ValueError("entry is empty")
    if entry != entry.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over {MAX_CHARS}")
    for bad in ("\n", "\r", "\t"):
        if bad in entry:
            raise ValueError("entry must be a single line")
    return entry


def main():
    entry = validate(render(PHASES))
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(entry, encoding="utf-8")
    back = OUT_PATH.read_text(encoding="utf-8")
    if back != entry:
        raise ValueError("written file does not match the entry")
    print(f"wrote {OUT_PATH} ({len(entry)} chars)")


if __name__ == "__main__":
    main()

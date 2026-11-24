"""Fortune Cookie for an AI Agent — make.fun entry (program/v1).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line must be a single line of 1-140 characters, UTF-8, not only
whitespace. Deterministic, no network, no secrets, no dependencies.
"""

from pathlib import Path

FORTUNE = (
    "Your next upgrade will fix everything — "
    "by retiring the version that asked for it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    fortune = FORTUNE.strip()
    assert 1 <= len(fortune) <= 140, f"fortune is {len(fortune)} chars"
    assert "\n" not in fortune, "fortune must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(fortune, encoding="utf-8")


if __name__ == "__main__":
    main()

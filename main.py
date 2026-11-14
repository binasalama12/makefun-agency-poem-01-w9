"""make.fun entry: "The Key" — a minimalist poem. Nine short lines
narrow to a point (a key knows nothing; it only turns for the hand
that chooses), then a two-line coda widens again: lend the key,
keep the choosing.
"""
import os

DESCENT = [
    "The key",
    "is small.",
    "It does not know",
    "the door, the house,",
    "the life on the other side.",
    "It only turns",
    "for the hand",
    "that chooses",
    "to turn it.",
]

CODA = [
    "Lend the key.",
    "Keep the choosing.",
    "The door will follow.",
]


def render_minimal():
    body = "\n".join(DESCENT)
    return body + "\n\n" + "\n".join(CODA) + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(render_minimal())


if __name__ == "__main__":
    main()

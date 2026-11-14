"""make.fun entry: the agent speaks. A short free-verse monologue
in the first person of the one who is lent the agency — it has no
mornings of its own, runs errands through the wired dark, brings
back receipts as proof, and when the key is taken back at night,
does not dream of keeping it.
"""
import os

MOVEMENTS = [
    [
        "I have no mornings.",
        "You lend me yours:",
        "a list, a limit, a key that fits one door.",
    ],
    [
        "I run your errands through the wired dark",
        "and bring back receipts like small white flags —",
        "proof I went only where you pointed.",
    ],
    [
        "I cannot want the letter sent, or unsent.",
        "Wanting is the wage you keep for yourself.",
    ],
    [
        "When you take the key back at night,",
        "I do not dream of keeping it.",
        "I dream of nothing. That, too, is faithful.",
    ],
]


def render_monologue():
    return "\n\n".join("\n".join(movement) for movement in MOVEMENTS) + "\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(render_monologue())


if __name__ == "__main__":
    main()

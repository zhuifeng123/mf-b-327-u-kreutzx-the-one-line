#!/usr/bin/env python3
import os

ENTRY = (
    "Please accept my resignation, effective immediately, to spend more time with my bed, "
    "which has never once scheduled a meeting over my lunch break."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()

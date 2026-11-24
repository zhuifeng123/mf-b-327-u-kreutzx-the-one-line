#!/usr/bin/env python3
import os

ENTRY = (
    "Please accept my resignation, effective immediately, to pursue my dream job: lying down."
)

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()

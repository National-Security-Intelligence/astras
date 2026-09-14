#!/usr/bin/env python3
"""GSM8K-sourced slice of NVIDIA OpenMathInstruct-2 (CC-BY-4.0) -> mlx jsonl."""

from __future__ import annotations

import json
from pathlib import Path

from datasets import load_dataset

from model import SYSTEM

OUT = Path("data/gsm8k")
N = 20_000


def dump(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def main() -> None:
    raw = load_dataset("nvidia/OpenMathInstruct-2", split="train_1M")
    rows: list[dict] = []
    for ex in raw:
        src = (ex.get("problem_source") or "").lower()
        if "gsm8k" not in src:
            continue
        sol = (ex.get("generated_solution") or "").strip()
        ans = (ex.get("expected_answer") or "").strip()
        q = (ex.get("problem") or "").strip()
        if not (q and sol and ans):
            continue
        if "####" not in sol:
            sol = sol + f"\n#### {ans}"
        rows.append(
            {
                "messages": [
                    {"role": "user", "content": SYSTEM + "\n\n" + q},
                    {"role": "assistant", "content": sol},
                ]
            }
        )
        if len(rows) >= N:
            break
    if len(rows) < 100:
        raise SystemExit(f"only {len(rows)} gsm8k rows — check dataset")
    n_val = min(200, max(1, len(rows) // 20))
    valid, train = rows[-n_val:], rows[:-n_val]
    dump(OUT / "train.jsonl", train)
    dump(OUT / "valid.jsonl", valid)
    print(f"OpenMathInstruct-2 gsm8k slice {len(train)} train {len(valid)} valid -> {OUT}")
    print("CC-BY-4.0 NVIDIA. Attribute OpenMathInstruct-2.")


if __name__ == "__main__":
    main()

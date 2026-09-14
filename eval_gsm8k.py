#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re

from datasets import load_dataset
from mlx_lm import generate, load

from model import STUDENT, SYSTEM

STRICT = re.compile(r"####\s*(-?[0-9][0-9,]*(?:\.[0-9]+)?)")
BOXED = re.compile(r"\\boxed\{([^}]+)\}")
LOOSE = re.compile(r"-?[0-9][0-9,]*(?:\.[0-9]+)?")


def nums(text: str) -> str:
    t = text.replace(",", "")
    s = STRICT.findall(t)
    if s:
        return s[-1]
    b = BOXED.findall(text)
    if b:
        m = LOOSE.findall(b[-1].replace(",", ""))
        if m:
            return m[-1]
    m = LOOSE.findall(t)
    return m[-1] if m else ""


def gold_num(answer: str) -> str:
    s = STRICT.findall(answer.replace(",", ""))
    return s[-1] if s else nums(answer)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--adapter", default="")
    p.add_argument("--sample", type=int, default=200, help="0 = full 1319")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--show", type=int, default=2)
    args = p.parse_args()

    adapter = args.adapter or None
    model, tok = load(STUDENT, adapter_path=adapter)
    test = load_dataset("openai/gsm8k", "main", split="test")
    if args.sample and args.sample < len(test):
        test = test.shuffle(seed=args.seed).select(range(args.sample))

    ok = 0
    n = len(test)
    print(f"Astras GSM8K n={n} {STUDENT} adapter={adapter or 'base'}")
    for i, ex in enumerate(test):
        messages = [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": ex["question"]},
        ]
        prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        text = generate(model, tok, prompt=prompt, max_tokens=1024, verbose=False)
        pred, gold = nums(text), gold_num(ex["answer"])
        ok += int(pred == gold and gold != "")
        if i < args.show:
            print("--- sample", i)
            print(text[-600:])
            print("pred", pred, "gold", gold)
        if (i + 1) % 10 == 0 or i + 1 == n:
            print(f"{i + 1}/{n}  {100 * ok / (i + 1):.1f}%")
    print(f"GSM8K: {ok}/{n} = {100 * ok / n:.2f}%  {STUDENT}")


if __name__ == "__main__":
    main()

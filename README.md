# Astras

Portable US reasoner: **Phi-4-mini-reasoning** (Microsoft, **MIT**, 3.8B, MLX 4-bit ~2.2 GB).

```bash
uv sync
uv run python eval_gsm8k.py --sample 200 --seed 0
```

Do **not** train until you have that baseline. Optional later: `uv run python train_sft.py` on OpenMathInstruct-2 (CC-BY-4.0).

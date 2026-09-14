# Astras

Open-source small reasoner. **Your** fine-tune. Training code is Apache-2.0.

Base weights for v0: [Gemma 3 1B Instruct](https://huggingface.co/google/gemma-3-1b-it) (Google), loaded as `mlx-community/gemma-3-1b-it-8bit` on Apple **MLX**. Gemma terms still apply to those weights. The name, scripts, and any adapter you train are Astras.

```bash
uv sync
uv run ruff check .
uv run python eval_gsm8k.py --sample 200 --seed 0
uv run python prepare_gsm8k.py
uv run python train_sft.py
```

`--sample 0` = full GSM8K test (1,319).

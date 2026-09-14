# Astras

Open-source small reasoner. Base: **Llama 3.2 3B Instruct** (Meta), Apple MLX.

```bash
uv sync
uv run ruff check .
uv run python eval_gsm8k.py --sample 200 --seed 0
```

4-bit MLX is ~1.8 GB on disk. First HF download may ask you to accept the Llama 3.2 license at huggingface.co/meta-llama/Llama-3.2-3B-Instruct.

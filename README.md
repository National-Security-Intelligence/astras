# Astras

Scripts for a portable MIT-licensed reasoner on Apple MLX.

**Weights are not in this repo.** You pull `mlx-community/Phi-4-mini-reasoning-4bit` (Microsoft Phi-4-mini-reasoning, MIT).

See [NOTICE.md](NOTICE.md) and [LICENSES.md](LICENSES.md).

```bash
uv sync
uv run python eval_gsm8k.py --sample 200 --seed 0
```

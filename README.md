# Astras

Lightweight student: **Gemma 3 1B** (~1.4 GB 8-bit MLX).
Math data: NVIDIA **OpenMathInstruct-2** GSM8K slice (**CC-BY-4.0**).

Not a live distill of OpenMath2-8B (that is Llama 3.1; the name would have to start with Llama).

Read [LICENSES.md](LICENSES.md).

```bash
git pull
uv sync
uv run python prepare_openmath.py
uv run python train_sft.py
uv run python eval_gsm8k.py --sample 200 --adapter outputs/sft
```

Baseline before train:

```bash
uv run python eval_gsm8k.py --sample 200 --seed 0
```

# Licenses — read this before you ship

None of the **weights** here are OSI open source. The **scripts** are Apache-2.0. The **NVIDIA dataset** is CC-BY-4.0.

| Piece | License | OSI? |
|---|---|---|
| `astras` scripts | Apache-2.0 | yes |
| Gemma 3 1B Instruct weights | [Gemma Terms of Use](https://ai.google.dev/gemma/terms) | **no** |
| OpenMath2-Llama3.1-8B weights | Llama 3.1 Community | **no** |
| OpenMathInstruct-2 data | CC-BY-4.0 | open data |

## Why we are not distilling the 8B into Gemma

OpenMath2-8B is a **Llama 3.1** model. Meta’s 3.1 license says: if you use Llama (or its outputs) to train another model you **distribute**, that model’s **name must start with “Llama”**, plus “Built with Llama.” Calling it Astras would not comply.

OpenMathInstruct-2 is the **same NVIDIA math work**, released **CC-BY-4.0**. It was generated with Llama-3.1-405B; NVIDIA published the text as CC-BY. Training Gemma on that **dataset** (not on live 8B generations) is the path that keeps the name Astras and does not load 8B on your Mac.

Gemma fine-tunes **stay under Gemma Terms**. You must pass those terms to users. This is not MIT/Apache weights.

If you still want live 8B→Gemma generation, say so. Then the distributed checkpoint would need a Llama-prefixed name.

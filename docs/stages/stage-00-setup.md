# Stage 0: Setup (1-2 days)

## Goal
A working environment where a small model answers a prompt on your machine.

## Read first
- Hugging Face: chat templating and text generation docs
- Hugging Face quantization docs (bitsandbytes 4-bit)

## Steps
1. Install Python 3.10+ and create a virtual environment.
2. `pip install -r requirements.txt`, then `pip freeze > requirements.lock` once it works.
3. Run `nvidia-smi` and note free GPU memory.
4. Load the model in 4-bit and generate one answer:

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL = "Qwen/Qwen2.5-Coder-0.5B-Instruct"   # use 1.5B once this works
bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16,
                         bnb_4bit_quant_type="nf4")
tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, quantization_config=bnb, device_map="auto")

msgs = [{"role": "user", "content": "Is this C function vulnerable?\n\nint f(char *s){char b[8]; strcpy(b,s); return 0;}"}]
ids = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(ids, max_new_tokens=200, do_sample=False)
print(tok.decode(out[0][ids.shape[1]:], skip_special_tokens=True))
```

5. Note the model's exact revision hash from its Hugging Face page.

## Learn only this
Tokenizers, chat templates, what 4-bit loading does to memory.

## Done when
You paste a C function into a script and the model replies.

## Pitfalls
- No GPU detected: check CUDA install and `torch.cuda.is_available()`.
- Out-of-memory: use the 0.5B model, close other GPU apps.

**Next:** [smoke test](../smoke-test.md), then [Stage 1](stage-01-data.md).

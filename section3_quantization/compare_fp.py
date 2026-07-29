import time
import psutil
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM
)

# -----------------------------
# Configuration
# -----------------------------

MODEL_NAME = "HuggingFaceTB/SmolLM2-360M-Instruct"

PROMPTS = [
    "Define AI.",
    "What is Python?",
    "What is Docker?",
    "What is RAG?",
    "Name one benefit of machine learning."
]

device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"\nUsing device: {device}")

# -----------------------------
# Load tokenizer
# -----------------------------

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# -----------------------------
# Load model (Full Precision)
# -----------------------------

start = time.perf_counter()

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

model.to(device)

load_time = time.perf_counter() - start

print(f"\nModel loaded in {load_time:.2f} sec")

# -----------------------------
# Memory
# -----------------------------

process = psutil.Process()

ram_mb = process.memory_info().rss / (1024 ** 2)

print(f"RAM Usage: {ram_mb:.2f} MB")

if device == "cuda":
    vram = torch.cuda.max_memory_allocated() / (1024 ** 2)
    print(f"GPU Memory: {vram:.2f} MB")

# -----------------------------
# Run prompts
# -----------------------------

results = []

for i, prompt in enumerate(PROMPTS, start=1):

    print(f"\nPrompt {i}")

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    ).to(device)

    start = time.perf_counter()

    outputs = model.generate(
        **inputs,
        max_new_tokens=40,
        do_sample=False
    )

    elapsed = time.perf_counter() - start

    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    generated_tokens = outputs.shape[1] - inputs["input_ids"].shape[1]

    tokens_per_second = generated_tokens / elapsed

    print(f"Time: {elapsed:.2f} sec")
    print(f"Speed: {tokens_per_second:.2f} tokens/sec")

    print("\nResponse:")
    print(answer)
    print("-" * 60)

    results.append({
        "prompt": prompt,
        "time": elapsed,
        "speed": tokens_per_second,
        "response": answer
    })

print("\nFinished Full Precision Benchmark.")
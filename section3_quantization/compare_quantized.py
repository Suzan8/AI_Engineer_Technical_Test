import time
import psutil
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig
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

print("\nLoading Quantized Model (4-bit NF4)...")

# -----------------------------
# Quantization Config
# -----------------------------

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True
)

# -----------------------------
# Load Tokenizer
# -----------------------------

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# -----------------------------
# Load Quantized Model
# -----------------------------

start = time.perf_counter()

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=bnb_config,
    device_map="auto"
)

load_time = time.perf_counter() - start

print(f"\nModel loaded in {load_time:.2f} sec")

# -----------------------------
# Memory Usage
# -----------------------------

process = psutil.Process()

ram_mb = process.memory_info().rss / (1024 ** 2)

print(f"RAM Usage: {ram_mb:.2f} MB")

if torch.cuda.is_available():
    gpu_mem = torch.cuda.max_memory_allocated() / (1024 ** 2)
    print(f"GPU Memory: {gpu_mem:.2f} MB")

# -----------------------------
# Benchmark
# -----------------------------

results = []

for i, prompt in enumerate(PROMPTS, start=1):

    print(f"\nPrompt {i}")

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

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

print("\nFinished Quantized Benchmark.")
# Section 3 – Quantization

## Objective

The goal of this section is to evaluate the impact of model quantization by comparing a full precision language model with a quantized version. The comparison focuses on memory consumption, inference speed, and response quality using the same model and the same evaluation prompts.

---

## Model

* **Model:** HuggingFaceTB/SmolLM2-360M-Instruct
* **Full Precision:** FP32 (CPU-only environment)
* **Quantized Version:** 4-bit (BitsAndBytes NF4)
---

## Project Structure
```
section3_quantization/
│
├── compare.py
├── compare_quantized.py
├── results.md
├── writeup.md
└── README.md
```

---

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Full Precision Benchmark

Execute:

```bash
python section3_quantization/compare_fp.py
```

This script:

* Loads the model in full precision (FP32).
* Measures model loading time.
* Measures RAM usage.
* Runs inference on five fixed prompts.
* Calculates tokens per second.
* Prints the generated responses.

---

## Running the Quantized Benchmark

Execute:

```bash
python section3_quantization/compare_quantized.py
```

This script:

* Loads the model using **BitsAndBytes 4-bit (NF4)** quantization.
* Measures model loading time.
* Measures RAM usage.
* Runs inference on the same five prompts.
* Calculates tokens per second.
* Prints the generated responses.

---

## Evaluation Metrics

The following metrics are compared between both versions:

* Model loading time
* Memory usage (RAM)
* Inference throughput (tokens/second)
* Response quality

---

## Outputs

The benchmark results are summarized in:

* **results.md** – Benchmark results and comparison table.
* **writeup.md** – Discussion of the trade-offs and deployment considerations.

---

## Notes

* The experiments were performed on a **CPU-only environment**.
* Since FP16/BF16 inference is primarily intended for GPU hardware, the full precision benchmark was executed using **FP32**.
* The quantized model used **BitsAndBytes 4-bit (NF4)** quantization.
* Due to hardware limitations, the quantized model reduced memory usage but did not improve inference speed.
* Both versions were evaluated using the same prompts to ensure a fair comparison.

---

## Expected Outcome

After completing this section, you will understand the trade-offs between full precision and 4-bit quantized models and how different quantization methods can affect deployment efficiency depending on the target hardware.

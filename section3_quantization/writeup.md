## Introduction

In this experiment, I evaluated the impact of model quantization by comparing a **Full Precision (FP32)** model with a **4-bit quantized model (BitsAndBytes - NF4)**. The objective was to analyze the trade-off between memory consumption, inference speed, and response quality while using the same model and the same evaluation prompts.

The evaluation was performed on a **CPU-only environment**. Since FP16/BF16 inference is primarily designed for GPU hardware, the full precision baseline was executed using **FP32**, while the quantized model was evaluated using **BitsAndBytes 4-bit (NF4)**.
---

## Experimental Observations

The quantized model reduced the memory footprint from approximately **1792 MB** to **1235 MB**, representing about a **31% reduction in RAM usage**. In addition, the model loading time was significantly reduced, decreasing from **247 seconds** to **9 seconds**.

Regarding inference performance, the full precision model achieved an average throughput of approximately **6.2 tokens per second**, while the quantized model achieved about **2.9 tokens per second**.Regarding inference performance, the full precision model achieved an average throughput of approximately **6.2 tokens per second**, while the quantized model achieved about **2.9 tokens per second**. Although quantization is generally expected to improve efficiency, this experiment was conducted on a **CPU-only environment**, where BitsAndBytes is primarily optimized for GPU execution. Consequently, the quantized model reduced memory usage but produced lower inference throughput than the FP32 baseline.

In terms of response quality, both models produced acceptable answers for simple prompts. However, the quantized model occasionally generated responses that were less accurate or less technically precise. For example, its explanation of Docker was less correct than the full precision version, while both models struggled to answer the RAG-related question because the selected language model is relatively small.

---

## Choosing a Quantization Method for Production

The choice of a quantization technique should depend primarily on the target deployment environment.

If the application is deployed on an **NVIDIA GPU** with limited VRAM, I would choose **BitsAndBytes (4-bit NF4)**. It integrates directly with the Hugging Face Transformers library, requires minimal implementation effort, and provides a good balance between memory efficiency and model quality.

For a production system where the model is already trained and inference speed is the highest priority, I would prefer **GPTQ** or **AWQ**. These methods perform quantization offline before deployment, allowing the model to be optimized for inference. In general, GPTQ focuses on improving inference latency, while AWQ often preserves model quality better by protecting the most important weights during quantization.

If the target environment is a **CPU-based server, personal computer, or edge device**, I would choose **GGUF** instead of BitsAndBytes. GGUF is specifically designed for efficient CPU inference through llama.cpp, making it a more suitable option for applications that do not rely on GPU acceleration.

---

## Conclusion

Based on this experiment, quantization successfully reduced memory consumption and significantly shortened model loading time. However, because the evaluation was performed on a CPU-only system, the 4-bit quantized model produced slower inference than the full precision model while introducing a slight reduction in response quality.

This experiment demonstrates that there is no universally best quantization method. The appropriate choice depends on the available hardware, memory constraints, inference speed requirements, and the acceptable trade-off between efficiency and model quality in the target production environment.

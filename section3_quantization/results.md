# Quantization Results

## Model

- **Model:** HuggingFaceTB/SmolLM2-360M-Instruct
- **Full Precision:** FP32
- **Quantized Version:** 4-bit (BitsAndBytes NF4)
- **Device:** CPU
- **PyTorch:** 2.13.0+cpu


# Benchmark Results

Precision vs. Size vs. Speed vs. Quality
Precision                   Memory     Usage	         Inference Speed	Output Quality
FP32 (Full Precision)	    1792 MB	   ~6.2 tokens/sec   Highest            quality and more accurate responses
4-bit NF4 (BitsAndBytes)    1235 MB	   ~2.9 tokens/sec	 Slight             quality degradation but acceptable for simple prompts



# Conclusion

The 4-bit quantized model significantly reduced memory consumption and loaded much faster than the full precision model.

However, on a CPU-only environment, inference throughput was lower than the FP32 model because 4-bit quantization is primarily optimized for GPU execution.

For lightweight deployment with limited memory, the quantized model is preferable.

For better response quality and faster CPU inference, the full precision model performed better in this experiment.
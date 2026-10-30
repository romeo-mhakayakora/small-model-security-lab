# Stage 10: Deployment (2+ weeks)

## Goal
A usable prototype with measured performance.

## Read first
llama.cpp GGUF conversion and quantization; vLLM docs; KV-cache memory explainers.

## Steps
1. Quantize the best model to GGUF with llama.cpp.
2. **Re-run the harness** on the quantized version.
3. Record for original, fine-tuned and quantized:

| Measure | Why |
|---|---|
| F1 with intervals | Did quantization hurt? |
| Peak memory | Fits target hardware? |
| Latency per example | Usable? |
| Throughput | Many assessments? |
| Cost per assessment | Real-world viability |

4. Only now consider vLLM for concurrent serving and Go services for a production control plane.

## Done when
You have an evidence-based deployment configuration for your target hardware.

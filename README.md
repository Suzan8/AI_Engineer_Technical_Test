# AI Engineer Technical Test

This repository contains my solutions for the AI Engineer Technical Assessment.

## Project Structure

```
AI_Engineer_Technical_Test/
│
├── section1_livekit/
│
├── section2_langchain_rag/
│
├── section3_quantization/
│
├── section4_deployment/
│
├── requirements.txt
├── README.md
├── .dockerignore
└── .env.example
```

## Sections

### Section 1 – LiveKit Voice Agent

- Voice Agent using LiveKit Agents
- STT → LLM → Tool Calling → TTS pipeline
- Mock order status tool
- Console-based text interaction
- Bonus provider swap explanation

More details are available in:

`section1_livekit/README.md`

---

### Section 2 – LangChain RAG

- Document ingestion
- Chunking
- FAISS Vector Store
- HuggingFace Embeddings
- Google Gemini
- Source-aware retrieval
- No-hallucination handling

More details are available in:

`section2_langchain_rag/README.md`

---

### Section 3 – Model Quantization

- Compared a full precision (FP32) language model with a 4-bit quantized version.
- Evaluated memory usage, model loading time, inference speed, and response quality.
- Benchmarked both models using the same prompts in a CPU-only environment.
- Included benchmark results and a discussion of quantization trade-offs.

More details are available in:

`section3_quantization/README.md`

---

### Section 4 – Deployment

- FastAPI REST API
- Streaming endpoint
- Docker support
- Load testing

More details are available in:

`section4_deployment/README.md`

---

## Installation

Install all project dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file from `.env.example`.

Example:

```
GOOGLE_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.5-flash
```

---

## Running

Each section contains its own README with detailed setup and execution instructions.
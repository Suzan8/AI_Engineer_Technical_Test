# Section 4 – Model Deployment

## Overview

This section deploys the Retrieval-Augmented Generation (RAG) pipeline implemented in **Section 2** as a REST API using **FastAPI**.

The service allows users to query indexed documents through HTTP endpoints and supports both standard and streaming responses. The application is containerized using Docker to simplify deployment.

---

## Features

* FastAPI REST API
* LangChain RAG integration
* FAISS vector database
* Google Gemini LLM
* Request validation using Pydantic
* Streaming responses
* Docker support
* Basic concurrent load testing

---

## Project Structure

```
section4_deployment/
│
├── app.py
├── Dockerfile
├── load_test.py
├── requirements.txt
├── README.md
└── writeup.md
```

---

## Requirements

* Python 3.13
* Google Gemini API Key
* Docker Desktop (optional)

---

## Installation

Clone the repository and install the dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root.

```text
GOOGLE_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

## Running the API

Start the FastAPI server.

```bash
python -m uvicorn section4_deployment.app:app --reload
```

The API will be available at

```
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET /

Health check endpoint.

Response

```json
{
    "message": "LangChain RAG API is running."
}
```

---

### POST /chat

Returns the complete generated answer.

Example request

```json
{
    "question": "What is the return policy?"
}
```

Example response

```json
{
    "answer": "Customers may return products within 30 days..."
}
```

---

### POST /chat/stream

Streams the generated response word-by-word using FastAPI's `StreamingResponse`.

Example request

```json
{
    "question": "What is the return policy?"
}
```

**Note**

Swagger UI waits until the full response is completed before displaying streamed content.

To observe real streaming behavior, use:

```bash
curl -N
```

or another streaming-capable HTTP client.

---

## Load Testing

A simple concurrent load test is provided.

Run

```bash
python section4_deployment/load_test.py
```

The script sends **10 concurrent requests** and reports:

* Average response time
* Fastest request
* Slowest request
* Total execution time
* HTTP status codes

---

## Docker

Build the Docker image

```bash
docker build -f section4_deployment/Dockerfile -t rag-api .
docker build --no-cache -f section4_deployment/Dockerfile -t rag-api .
```

Run the container

```bash
docker run -p 8000:8000 rag-api
```

---

## Technologies Used

* Python
* FastAPI
* LangChain
* FAISS
* HuggingFace Embeddings
* Google Gemini
* Docker
* Uvicorn
* Requests

---

## Limitations

* The API depends on Google Gemini API availability and quota.
* Streaming is simulated by progressively sending the generated response after inference completes.
* The current implementation is intended for demonstration purposes and has not been optimized for high-throughput production workloads.

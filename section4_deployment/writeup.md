# Section 4 Write-up

## Deployment Choice

The model was deployed as a REST API using **FastAPI** because it is lightweight, easy to develop, and well suited for serving machine learning models. FastAPI also provides automatic API documentation through Swagger UI and supports asynchronous request handling, making it a practical choice for this project.

The application exposes two endpoints:

* `/chat` for standard responses.
* `/chat/stream` for streaming responses using FastAPI's `StreamingResponse`.

The API integrates the Retrieval-Augmented Generation (RAG) pipeline developed in Section 2, which retrieves relevant document chunks from a FAISS vector store before generating answers with Google Gemini.

A Dockerfile is included to package the application and simplify deployment across different environments.

---

## Scaling to 50 Concurrent Users

If this service needed to support approximately 50 concurrent users in production, several improvements would be introduced.

First, the API would be deployed behind multiple FastAPI workers using Gunicorn or Uvicorn workers together with a reverse proxy such as Nginx.

Second, frequently requested questions could be cached using Redis to reduce repeated LLM calls and improve response latency.

A request queue (such as Celery or RabbitMQ) could be used to process long-running requests without blocking API workers.

Horizontal autoscaling with Kubernetes or another orchestration platform would allow additional application instances to be created automatically under heavy load.

Finally, monitoring tools such as Prometheus and Grafana would be added to continuously track latency, throughput, resource utilization, and error rates, enabling proactive scaling and performance optimization.

These improvements would significantly increase system reliability, throughput, and scalability while maintaining acceptable response times under higher workloads.

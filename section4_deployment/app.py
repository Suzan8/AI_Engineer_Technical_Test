from pathlib import Path
import sys
from fastapi.responses import StreamingResponse
import time

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Add Section 2 source folder
SECTION2_SRC = (
    Path(__file__).resolve().parent.parent
    / "section2_langchain_rag"
    / "src"
)

sys.path.insert(0, str(SECTION2_SRC))

from rag_pipeline import ask

app = FastAPI(
    title="LangChain RAG API",
    version="1.0.0",
    description="RAG Chatbot API using LangChain, FAISS and Google Gemini."
)


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@app.get("/")
def root():
    return {
        "message": "LangChain RAG API is running."
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    answer, _ = ask(question)

    return ChatResponse(answer=answer)


@app.post("/chat/stream")
def chat_stream(request: ChatRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    answer, _ = ask(question)

    def generate():
        for word in answer.split():
            yield word + " "
            time.sleep(0.05)

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )
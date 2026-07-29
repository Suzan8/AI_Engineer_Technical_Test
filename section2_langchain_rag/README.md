# LangChain RAG Chatbot

A simple Retrieval-Augmented Generation (RAG) chatbot built with:

- LangChain
- Google Gemini
- FAISS
- HuggingFace Embeddings

The chatbot retrieves relevant information from local documents before generating an answer.

---

# Project Structure

```
section2_langchain_rag
│
├── data/
├── vectorstore/
├── src/
├── requirements.txt
└── README.md
```

---

# Features

- Load PDF, Markdown, and Text files
- Split documents into chunks
- Generate embeddings using HuggingFace
- Store embeddings in FAISS
- Retrieve relevant context
- Generate answers using Google Gemini

---

# Supported Document Types

- PDF (.pdf)
- Markdown (.md)
- Text (.txt)

---

# Installation

## 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**Command Prompt**

```cmd
.venv\Scripts\activate
```

---

## 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install PyTorch (CPU)

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

---

## 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# Build the Vector Database

Run:

```bash
python section2_langchain_rag/src/ingest.py
```

Re-run this command whenever documents are added or modified.

---

# Start the Chatbot

```bash
python section2_langchain_rag/src/chatbot.py
```

---

# Add New Documents

Place your files inside:

```
section2_langchain_rag/data/
```

Supported formats:

- .pdf
- .md
- .txt

Then rebuild the vector database:

```bash
python section2_langchain_rag/src/ingest.py
```

---

# Example Questions

### Return Policy

- What is the return policy?
- Can I return a customized product?
- How many days do I have to return an item?

### Product Catalog

- What is the price of Laptop Pro X15?
- Which product has the longest warranty?
- Tell me about AirSound Pro Earbuds.

### FAQ

- What payment methods are accepted?
- How long does shipping take?
- Can I cancel my order?
- How can I contact customer support?

### Out-of-Scope Questions

- Who is the CEO of Microsoft?
- What is the capital of Egypt?

---

# Technologies

- Python
- LangChain
- Google Gemini
- HuggingFace Embeddings
- FAISS
- PyTorch

---

# Notes

- Rebuild the FAISS index after updating documents.
- The chatbot answers using only the indexed documents.
- A valid Google Gemini API key is required.
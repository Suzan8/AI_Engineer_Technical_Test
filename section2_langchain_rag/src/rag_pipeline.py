from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from config import MODEL_NAME


from config import VECTORSTORE_DIR, EMBEDDING_MODEL

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = FAISS.load_local(
    str(VECTORSTORE_DIR),
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    temperature=0
)


def ask(question: str):

    docs = retriever.invoke(question)

    if len(docs) == 0:
        return "No relevant context found.", []

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.

If the answer is not present in the context,
reply exactly:

I couldn't find relevant information in the provided documents.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content, docs
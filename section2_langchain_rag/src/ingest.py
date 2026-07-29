from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    DATA_DIR,
    VECTORSTORE_DIR,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def load_documents():

    docs = []

    for file in DATA_DIR.iterdir():

        if file.suffix.lower() == ".pdf":

            docs.extend(PyPDFLoader(str(file)).load())

        elif file.suffix.lower() in [".md", ".txt"]:

            docs.extend(TextLoader(str(file), encoding="utf-8").load())

    return docs


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,

        chunk_overlap=CHUNK_OVERLAP,

    )

    return splitter.split_documents(documents)


def build_vectorstore(chunks):

    embeddings = HuggingFaceEmbeddings(

        model_name=EMBEDDING_MODEL

    )

    db = FAISS.from_documents(

        chunks,

        embeddings

    )

    VECTORSTORE_DIR.mkdir(exist_ok=True)

    db.save_local(str(VECTORSTORE_DIR))

    print(f"\nSaved {len(chunks)} chunks successfully.")


def main():

    print("Loading documents...")

    docs = load_documents()

    print(f"Loaded {len(docs)} documents.")

    print("Splitting documents...")

    chunks = split_documents(docs)

    print(f"Created {len(chunks)} chunks.")

    print("Building FAISS index...")

    build_vectorstore(chunks)

    print("Done.")


if __name__ == "__main__":

    main()
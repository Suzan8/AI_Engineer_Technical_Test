## Introduction

The implemented RAG (Retrieval-Augmented Generation) pipeline works well for a small collection of documents by retrieving the most relevant text chunks before generating an answer. The current implementation uses FAISS as the vector database, HuggingFace embeddings for semantic search, and Google Gemini as the language model.

## Improving the Chunking Strategy

The current system splits documents using RecursiveCharacterTextSplitter with a fixed chunk size and overlap. While this approach is suitable for small datasets, it may not always provide the best results for larger documents.

To improve performance, I would experiment with different chunk sizes and overlap values. Larger chunks preserve more context, while smaller chunks can improve retrieval precision. Selecting the right values depends on the document type and content.

## Improving the Retrieval Process

The current implementation uses semantic similarity search with FAISS. For larger document collections, I would replace it with a hybrid retrieval approach that combines semantic search with keyword search (such as BM25).

This combination helps retrieve relevant information even when the user's query contains exact keywords that may not be well represented by embeddings alone.

## Adding a Re-ranking Step

Another improvement would be adding a re-ranking stage after retrieving the initial results. Instead of directly sending the retrieved chunks to the LLM, a re-ranker would sort them according to their relevance to the user's question.

This ensures that the language model receives the most useful context, leading to more accurate answers.

## Additional Enhancements

If the document collection grows larger, I would also consider:

Using metadata filtering to retrieve documents from specific sources or categories.
Increasing the number of retrieved chunks when necessary.
Using query expansion or multiple search queries to improve recall.
Monitoring retrieval quality and adjusting chunking parameters based on evaluation results.

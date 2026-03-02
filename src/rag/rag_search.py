from src.vectorstore.retriever import get_relevant_docs


def rag_search(query: str, k: int = 3) -> str:
    """
    Run a RAG search:
    - Retrieve the most relevant documents using the vectorstore retriever
    - Combine their content into a single string
    - Return the context ready to be used by the agent/LLM

    Args:
        query (str): User query.
        k (int): Number of documents to retrieve.

    Returns:
        str: Combined text content of the retrieved documents.
    """
    docs = get_relevant_docs(query, k=k)

    if not docs:
        return ""

    combined_context = "\n\n".join(doc.page_content for doc in docs)
    return combined_context

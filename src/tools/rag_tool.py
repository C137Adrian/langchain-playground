from langchain.tools import tool
from src.rag.rag_search import rag_search

@tool("rag_tool", return_direct=False)
def rag_tool(query: str) -> str:
    """
    Tool that retrieves relevant context using the RAG pipeline.
    """
    context = rag_search(query)
    return context if context else "No relevant context found."

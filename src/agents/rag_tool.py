from langchain.tools import tool
from src.rag.rag_search import rag_search


@tool("rag_search", return_direct=False)
def rag_tool(query: str) -> str:
    """
    Agent tool that retrieves relevant context using the RAG pipeline.
    The agent can call this tool when additional context is needed.
    
    Args:
        query (str): User query.
    
    Returns:
        str: Retrieved context or a fallback message.
    """
    context = rag_search(query)
    if not context:
        return "No relevant context found."
    return context

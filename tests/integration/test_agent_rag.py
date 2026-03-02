from src.agents.multi_tool_agent import agent

def test_agent_rag_integration():
    """
    Validates that the agent can retrieve contextual information from the vectorstore.
    """
    query = "Explain the content stored in the vectorstore"
    response = agent(query)

    assert isinstance(response, str)
    assert "LangChain" in response or "RAG" in response or "Groq" in response

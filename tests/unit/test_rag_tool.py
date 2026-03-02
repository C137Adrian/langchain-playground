from src.tools.rag_tool import rag_tool

def test_rag_tool_returns_context():
    result = rag_tool.invoke({"query": "LangChain"})
    assert isinstance(result, str)
    assert len(result) > 0

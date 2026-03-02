from src.agents.multi_tool_agent import build_multi_tool_agent

def test_agent_initialization():
    """
    Ensures the agent initializes correctly and exposes a callable interface.
    """
    agent = build_multi_tool_agent()

    # The agent must be callable
    assert callable(agent)

    # The agent must return a string when invoked with a simple query
    response = agent("hello")
    assert isinstance(response, str)
    assert len(response) > 0

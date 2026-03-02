from src.tools.time_tools import get_current_time

def test_get_current_time():
    result = get_current_time.invoke({})
    assert isinstance(result, str)
    assert len(result) > 0

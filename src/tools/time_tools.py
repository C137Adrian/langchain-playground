from langchain.tools import tool
from datetime import datetime

@tool
def get_current_time() -> str:
    """Return the current server time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

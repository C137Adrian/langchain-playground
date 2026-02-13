from langchain.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

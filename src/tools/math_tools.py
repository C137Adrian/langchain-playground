from langchain.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def subtract_numbers(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

@tool
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

@tool
def divide_numbers(a: int, b: int) -> float:
    """Divide a by b."""
    if b == 0:
        return "Error: division by zero"
    return a / b

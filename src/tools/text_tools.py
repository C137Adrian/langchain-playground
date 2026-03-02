from langchain.tools import tool

@tool
def reverse_text(text: str) -> str:
    """Reverse the given text."""
    return text[::-1]

@tool
def count_words(text: str) -> int:
    """Count the number of words in the text."""
    return len(text.split())

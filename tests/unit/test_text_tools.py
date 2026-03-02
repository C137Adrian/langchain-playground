from src.tools.text_tools import reverse_text, count_words

def test_reverse_text():
    assert reverse_text.invoke({"text": "hello"}) == "olleh"

def test_count_words():
    assert count_words.invoke({"text": "hola mundo"}) == 2

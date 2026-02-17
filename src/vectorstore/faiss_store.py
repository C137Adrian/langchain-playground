import faiss
from langchain_community.vectorstores import FAISS
from src.embeddings.embeddings import get_embeddings

def create_faiss_store(texts: list[str]):
    """
    Creates a FAISS vector store from a list of texts.
    """
    embeddings = get_embeddings()
    return FAISS.from_texts(texts, embedding=embeddings)

def load_faiss_store(path: str):
    """
    Loads an existing FAISS index from disk.
    """
    embeddings = get_embeddings()
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

def save_faiss_store(store: FAISS, path: str):
    """
    Saves the FAISS index to disk.
    """
    store.save_local(path)

from langchain_community.vectorstores import FAISS
from src.embeddings.embeddings import get_embeddings

INDEX_PATH = "faiss_index"

def load_faiss_store():
    """
    Loads the FAISS index from disk using the same embedding model.
    """
    embeddings = get_embeddings()
    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

def get_retriever(k: int = 3):
    """
    Returns a retriever object that can be used to search the FAISS index.
    """
    faiss_store = load_faiss_store()
    return faiss_store.as_retriever(search_kwargs={"k": k})

def get_relevant_docs(query: str, k: int = 3):
    """
    Retrieves the top-k most relevant documents for a given query.
    """
    retriever = get_retriever(k)
    return retriever.invoke(query)


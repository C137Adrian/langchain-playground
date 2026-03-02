from src.vectorstore.faiss_store import create_faiss_store, save_faiss_store

def build_index():
    # Example documents
    docs = [
        "LangChain uses tools and function calling.",
        "Groq provides extremely fast inference for Llama models.",
        "RAG improves LLM responses by retrieving relevant context."
    ]

    store = create_faiss_store(docs)
    save_faiss_store(store, "faiss_index")

if __name__ == "__main__":
    build_index()

from src.vectorstore.retriever import get_relevant_docs

def test_retriever():
    print("\n=== TEST RETRIEVER ===\n")

    query = "¿Qué es LangChain?"
    docs = get_relevant_docs(query)

    assert len(docs) > 0, "El retriever no devolvió documentos"

    for i, d in enumerate(docs, start=1):
        print(f"\n--- Documento {i} ---\n")
        print(d.page_content)

if __name__ == "__main__":
    test_retriever()

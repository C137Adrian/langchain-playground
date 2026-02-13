from chains.explain_and_summarize import build_explain_and_summarize_chain


def main():
    chain = build_explain_and_summarize_chain()

    topic = "LangChain"
    result = chain(
        {"topic": topic}
    )

    print("=== Explanation ===")
    print(result["explanation"])
    print("\n=== Summary ===")
    print(result["summary"])


if __name__ == "__main__":
    main()

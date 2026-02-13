from chains.memory_chain import build_memory_chain


def main():
    chain = build_memory_chain()

    print(chain.run("Hi, my name is Adrian."))
    print(chain.run("Can you remind me what my name is?"))


if __name__ == "__main__":
    main()

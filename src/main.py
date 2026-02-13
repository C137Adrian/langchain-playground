from agents.math_agent import build_math_agent

def main():
    agent = build_math_agent()
    result = agent("What is 12 + 30?")
    print(result)

if __name__ == "__main__":
    main()

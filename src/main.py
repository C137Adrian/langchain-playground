from src.agents.multi_tool_agent import build_multi_tool_agent

def main():
    agent = build_multi_tool_agent()

    print("Agente listo. Escribe 'exit' para salir.\n")

    while True:
        user_input = input("Tú: ")

        if user_input.lower() in ["exit", "quit", "salir"]:
            print("Agente: Hasta luego!")
            break

        response = agent(user_input)
        print(f"Agente: {response}\n")

if __name__ == "__main__":
    main()

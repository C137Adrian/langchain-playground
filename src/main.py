from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def main():
    llm = ChatGroq(model="llama-3.1-8b-instant")

    response = llm.invoke("Hola, ¿estás funcionando con Llama 3.1 en Groq?")
    print(response)

if __name__ == "__main__":
    main()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_groq import ChatGroq 
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from dotenv import load_dotenv 

load_dotenv()

def build_memory_chain():
    llm = ChatGroq(model="llama-3.1-8b-instant")

    memory = ConversationBufferMemory(return_messages=True)

    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True,
    )

    return chain

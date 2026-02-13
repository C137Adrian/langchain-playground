from langchain_groq import ChatGroq
from tools.math_tools import add_numbers
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

def build_math_agent():
    llm = ChatGroq(model="llama-3.1-8b-instant")

    # Bind tools to the model
    llm_with_tools = llm.bind_tools([add_numbers])

    def agent(query: str):
        # Send the user message
        response = llm_with_tools.invoke([HumanMessage(content=query)])

        # If the model wants to call a tool
        if response.tool_calls:
            tool_call = response.tool_calls[0]
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            # Execute the tool
            if tool_name == "add_numbers":
                return add_numbers.invoke(tool_args)

        # If no tool call, return normal text
        return response.content

    return agent

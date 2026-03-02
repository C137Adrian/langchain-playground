from langchain_core.messages import HumanMessage, SystemMessage
from src.tools.math_tools import (
    add_numbers, subtract_numbers, multiply_numbers, divide_numbers
)
from src.tools.text_tools import reverse_text, count_words
from src.tools.time_tools import get_current_time
from src.tools.rag_tool import rag_tool
from src.llm.groq import get_llm

def build_multi_tool_agent():

    llm = get_llm()

    # List of available tools
    tools = [
        add_numbers,
        subtract_numbers,
        multiply_numbers,
        divide_numbers,
        reverse_text,
        count_words,
        get_current_time,
        rag_tool
    ]

    # Bind tools to the model (function calling)
    llm_with_tools = llm.bind_tools(tools)

    # System instruction
    system_prompt = SystemMessage(content="""
You are an AI assistant with access to a limited set of tools.
You must follow these rules:

1. You can ONLY use the tools explicitly provided to you.
2. If a tool is not listed, you MUST NOT attempt to call it.
3. Use the RAG tool only when the user asks about information that may exist
   inside the vectorstore (documents, notes, stored knowledge).
4. If the question is general knowledge or can be answered directly,
   respond normally without calling any tool.
5. When you decide to call a tool, respond ONLY with a JSON object containing
   the tool name and its arguments.
""")

    def agent(user_input: str):

        # Only send system + user message (no memory)
        messages = [
            system_prompt,
            HumanMessage(content=user_input)
        ]

        response = llm_with_tools.invoke(messages)

        # If the model wants to call a tool
        if response.tool_calls:
            tool_call = response.tool_calls[0]
            name = tool_call["name"]
            args = tool_call["args"]

            # Find and execute the tool
            for tool in tools:
                if tool.name == name:
                    context = tool.invoke(args)
                    return f"According to the retrieved context:\n\n{context}"


        # Otherwise return normal text
        return response.content

    return agent

# GLOBAL AGENT INSTANCE
agent = build_multi_tool_agent()
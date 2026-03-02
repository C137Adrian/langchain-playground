from langchain_core.messages import HumanMessage, SystemMessage
from src.tools.math_tools import (
    add_numbers, subtract_numbers, multiply_numbers, divide_numbers
)
from src.tools.text_tools import reverse_text, count_words
from src.tools.time_tools import get_current_time
from src.agents.rag_tool import rag_tool
from llm.groq import get_llm

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
You are an AI assistant that can only use the tools explicitly provided to you.
If a tool is not listed in the current toolset, you MUST NOT attempt to call it.

If the user asks a general knowledge question, answer directly without calling any tool.
Use the RAG tool only when the question requires retrieving context from the vectorstore.

When you decide to call a tool, respond ONLY with a JSON object containing
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
                    return tool.invoke(args)

        # Otherwise return normal text
        return response.content

    return agent

# GLOBAL AGENT INSTANCE
agent = build_multi_tool_agent()
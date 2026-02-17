from langchain_core.messages import HumanMessage, SystemMessage
from src.tools.math_tools import (
    add_numbers, subtract_numbers, multiply_numbers, divide_numbers
)
from src.tools.text_tools import reverse_text, count_words
from src.tools.time_tools import get_current_time
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
        get_current_time
    ]

    # Bind tools to the model (function calling)
    llm_with_tools = llm.bind_tools(tools)

    # System instruction
    system_prompt = SystemMessage(content="""
You are an AI assistant that uses tools through JSON function calling.
When you decide to call a tool, respond only with a JSON object containing
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

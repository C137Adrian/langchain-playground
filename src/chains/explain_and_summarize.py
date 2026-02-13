from langchain_core.prompts import PromptTemplate 
from langchain_classic.chains import LLMChain, SequentialChain 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv
load_dotenv()


def build_explain_and_summarize_chain():
    llm = ChatGroq(model="llama-3.1-8b-instant")

    # Primer paso: explicación
    explain_prompt = PromptTemplate(
        input_variables=["topic"],
        template="Explain the concept of {topic} in clear and simple terms."
    )
    explain_chain = LLMChain(
        llm=llm,
        prompt=explain_prompt,
        output_key="explanation",
    )

    # Segundo paso: resumen
    summarize_prompt = PromptTemplate(
        input_variables=["explanation"],
        template="Summarize the following explanation in 3 bullet points:\n\n{explanation}"
    )
    summarize_chain = LLMChain(
        llm=llm,
        prompt=summarize_prompt,
        output_key="summary",
    )

    # Encadenar los pasos
    overall_chain = SequentialChain(
        chains=[explain_chain, summarize_chain],
        input_variables=["topic"],
        output_variables=["explanation", "summary"],
    )

    return overall_chain

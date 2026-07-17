from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

def demo_basic_chain():
    
    # Basic chain
    # prompt = ChatPromptTemplate.from_template("You are a helpful assitant. Answer the following in one sentence {question} ")
    # model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    # parser = StrOutputParser()
    # chain = prompt | model | parser
    # result = chain.invoke({"question": "what is tanstack"})

    # Batch execution

    prompt = ChatPromptTemplate.from_template("write a story: {topic}")
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    parser = StrOutputParser()
    chain = prompt | model | parser

    # inputs = [
    #     {"text", "do you want a tea or coffee?"},
    #     {"text", "I want milk"},
    # ];

    # result = chain.batch(inputs)
    # print(result)

    # Output string
    for chunk in chain.stream({"topic": "clever fox"}):
        print(chunk, end="", flush=True)



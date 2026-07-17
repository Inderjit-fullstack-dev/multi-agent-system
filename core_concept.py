from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import init_chat_model
# load_dotenv()

def demo_basic_chain():

    # Basic chain
    # prompt = ChatPromptTemplate.from_template("You are a helpful assitant. Answer the following in one sentence {question} ")
    # model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    # parser = StrOutputParser()
    # chain = prompt | model | parser
    # result = chain.invoke({"question": "what is tanstack"})

    # Batch execution

    prompt = ChatPromptTemplate.from_template("write a story: {topic}")
    model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens = 1000, max_retries = 4)
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



def new_way_to_init_model():

    prompt = ChatPromptTemplate.from_template("You are a helpful english assistant. Answer the following in one sentence {question} ")
    model = init_chat_model(model="gpt-4o-mini", temperature=0.7, max_tokens=4096)
    parser = StrOutputParser()
    chain = prompt | model | parser
    result = chain.invoke({"question": "when to use \"how\" in english, explain with giving 2 examples"})
    print(result)

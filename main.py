
from dotenv import load_dotenv

from core_concept import demo_basic_chain, new_way_to_init_model

# it will automaticaly load the env variables
load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


def main():

    # llm = ChatOpenAI(model="gpt-4o-mini")
    # # Use a valid Claude model name
    # anthropic_llm = ChatAnthropic(
    #     model="claude-haiku-4-5-20251001"
    # )  # ✅ Latest Claude 3.5 Sonnet

    # response_openai = llm.invoke("Hello, how are you?")
    # response_anthropic = anthropic_llm.invoke("Hello, how are you?")

    # print(response_openai.content)
    # print(response_anthropic.content)

    #demo_basic_chain()
    #
    new_way_to_init_model()


if __name__ == "__main__":
    main()

import os

from dotenv import load_dotenv

from core_concept import demo_basic_chain

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


def main():
    # openai_key = os.getenv("OPENAI_API_KEY")
    # anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    # print(f"OpenAI API Key loaded: {bool(openai_key)}")
    # print(f"Anthropic API Key loaded: {bool(anthropic_key)}")

    # llm = ChatOpenAI(model="gpt-4o-mini")
    # # Use a valid Claude model name
    # anthropic_llm = ChatAnthropic(
    #     model="claude-haiku-4-5-20251001"
    # )  # ✅ Latest Claude 3.5 Sonnet

    # response_openai = llm.invoke("Hello, how are you?")
    # response_anthropic = anthropic_llm.invoke("Hello, how are you?")

    # print(response_openai.content)
    # print(response_anthropic.content)

    demo_basic_chain()


if __name__ == "__main__":
    main()

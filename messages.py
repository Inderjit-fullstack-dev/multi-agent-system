from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

#load the env
from dotenv import load_dotenv
load_dotenv()

def messages_demo():
    model = init_chat_model("gpt-4o-mini")
    system_msg = SystemMessage("You are a helpful assistant.")
    human_msg = HumanMessage("Hello, how are you?")

    messages = [system_msg, human_msg]
    response = model.invoke(messages)

    messages.append(response)
    print(messages)

if __name__ == "__main__":
    messages_demo()

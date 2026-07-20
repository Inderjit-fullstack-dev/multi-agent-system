from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, AIMessage, SystemMessage

#load the env
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser, format_instructions
from langchain_openai import ChatOpenAI
from pydantic import Field, BaseModel

load_dotenv()

# def messages_demo():
#     model = init_chat_model("gpt-4o-mini")
#     system_msg = SystemMessage("You are a helpful assistant.")
#     human_msg = HumanMessage("Hello, how are you?")

#     messages = [system_msg, human_msg]
#     response = model.invoke(messages)

#     messages.append(response)
#     print(messages)

'''
    using prompt templates
'''


# from langchain_core.prompts import ChatPromptTemplate
# template = ChatPromptTemplate([
#     ("system", "You are an expert american english teacher and Your name is {name}."),
#     ("human", "{question}")
# ])

# # create the prompt. It will not call actual ai
# prompt = template.invoke({
#     "name": "Superman",
#     "question": "What is a pronoun?"
# })

# model = init_chat_model("gpt-4o-mini")

# response = model.invoke(prompt)
# print(response)



from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# 1. Define your examples
# examples = [
#     {"input": "I loved this product!", "output": "Positive"},
#     {"input": "Worst experience ever.", "output": "Negative"},
#     {"input": "It was okay, nothing special.", "output": "Neutral"},
# ]
#
# # 2. Create the example prompt template
# example_prompt = ChatPromptTemplate([
#     ("human", "Review: {input}"),
#     ("ai", "Sentiment: {output}")
# ])
#
# # 3. Create the few-shot prompt
# few_shot_prompt = FewShotChatMessagePromptTemplate(
#     examples= examples,
#     example_prompt= example_prompt,
# )
#
# print(few_shot_prompt)
#
#
# # 4. Combine with the main prompt
# final_prompt = ChatPromptTemplate([
#     ("system", "You are a sentiment analyzer."),
#     few_shot_prompt,  # Examples go here
#     ("human", "Review: {new_review}\nSentiment:")
# ])
#
# # 5. Use it
# chain = final_prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()
# result = chain.invoke({"new_review": "I do not like this song."})
# # Output: "Positive"
#
# print(result)


#parser examples
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")

#parser = StrOutputParser() # string parser
#parser = JsonOutputParser()

parser = PydanticOutputParser(pydantic_object=Person) # bind result with class model
prompt = (ChatPromptTemplate.from_template("Give me name and age from the {description} in json")
          .partial(format_instructions = parser.get_format_instructions()))
model = ChatOpenAI(model="gpt-4o-mini")
chain = prompt | model | parser
result = chain.invoke({
    "description": "My name is Inder and i am 30 years old"
})

# Structure Output (Best way to do it)

class MovieReview(BaseModel):
    title: str = Field(description="Title of the movie")
    review: str = Field(description="Review of the movie")
    rating: int = Field(description="Rating of the movie out of 10")

structured_model = model.with_structured_output(MovieReview)
res = structured_model.invoke("Review: Inception is a fantastic movie with rating of 9")
print(res)






















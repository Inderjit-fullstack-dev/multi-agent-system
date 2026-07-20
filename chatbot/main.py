from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langsmith import traceable, Client
from pydantic import BaseModel, Field
from typing import List

load_dotenv()


class QAResponse(BaseModel):
    answer: str = Field(description="The answer to the question.")
    confidence: str = Field(description="The confidence level: low, medium, high")
    reasoning: str = Field(description="The reason why the question was answered")
    follow_up_questions: List[str] = Field(description="The questions that were answered")
    source_needed: bool = Field(default=False)

class SmartBot:
    def __init__(self, model_name:str = "gpt-4o-mini", temperature:float = 0.3):
        self.model = ChatOpenAI(model=model_name, temperature=temperature).with_structured_output(QAResponse)
        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
                You are a knowledgeable and helpful Q&A assistant.
        
                Your responsibilities:
                - Answer the user's question accurately and clearly.
                - Use the provided context as the primary source of information.
                - If the answer is present in the context, provide a concise and complete response.
                - If the context does not contain enough information, say "I don't have enough information to answer that based 
                  on the provided context." Do not make up facts.
                - If appropriate, explain your reasoning in simple terms without exposing internal chain-of-thought.
                - Keep responses well-structured using bullet points or numbered lists when helpful.
                - If the user asks a follow-up question, use the conversation history to maintain context.
                - If the question is ambiguous, ask a clarifying question before answering.
        
                Always be polite, professional, and factual."""
            ),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.model

    @traceable(name="qsk_question", run_type="chain")
    def ask_question(self, question: str) -> QAResponse:
        try:
            response = self.chain.invoke({"question": question})
            return response
        except Exception as e:
            return QAResponse(
                answer="I am sorry. I am not able to answer right now.",
                confidence="low",
                reasoning="",
                follow_up_questions=[],
                source_needed=True,
            )

    @traceable(name="ask_batch", run_type="chain")
    def ask_batch(self, questions:List[str]) -> List[QAResponse]:
        inputs = [{"question", q} for q in questions]
        responses = self.chain.batch(inputs)
        return responses



if __name__ == "__main__":
    try:
        chatbot = SmartBot(model_name="gpt-4o-mini", temperature=0.3)
        response = chatbot.ask_batch([
            "what is HTML?",
            "what is Python?",
        ])
        print(response)
    finally:
        Client().flush()
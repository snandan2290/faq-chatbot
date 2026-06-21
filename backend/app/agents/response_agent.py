# app/agents/response_agent.py

from app.services.llm_service import LLMService


class ResponseAgent:
    def __init__(self):

        self.llm = LLMService()

    def generate_response(self, history, faq_context, question):

        prompt = f"""
You are a customer support chatbot.

Conversation History:
{history}

FAQ Context:
{faq_context}

Current Question:
{question}

Rules:

1. Answer only from FAQ Context.
2. If FAQ Context is empty say:
   "I could not find information in the FAQ."
3. Never hallucinate.
4. Keep answers concise.
5. Do not make up answers.

Response:
"""
        print(f"prompt::{prompt}")
        return self.llm.ask(prompt)

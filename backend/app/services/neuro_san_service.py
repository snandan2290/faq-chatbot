from neuro_san.client.agent_session_factory import DirectAgentSessionFactory
from dotenv import load_dotenv
import os
from .faq_service import FAQService

load_dotenv()


class NeuroSANService:
    def __init__(self):

        # print("AGENT_MANIFEST_FILE =", os.getenv("AGENT_MANIFEST_FILE"))
        # print("OPENAI:", os.getenv("OPENAI_API_KEY") is not None)

        self.factory = DirectAgentSessionFactory()
        self.faq_service = FAQService()

    def ask(self, message: str):

        session = self.factory.create_session(
            agent_name="faq_chatbot", use_direct=True, metadata={}
        )

        # request_payload = {"user_message": {"text": message}}
        faq_context = self.faq_service.build_context()

        request_payload = {
            "user_message": {
                "text": f"""
        FAQ Context:

        {faq_context}

        User Question:

        {message}

        Answer only using FAQ Context.

        If answer is unavailable say:

        I could not find information in the FAQ.
        """
            }
        }
        # print(f"request_payload:::{request_payload}")
        stream = session.streaming_chat(request_payload)

        responses = []

        for msg in stream:
            responses.append(msg)

            if msg.get("done") is True:
                break

        return responses[-1]["response"]["text"]

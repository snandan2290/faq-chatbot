from app.agents.conversation_agent import ConversationAgent
from app.agents.retriever_agent import RetrieverAgent
from app.agents.response_agent import ResponseAgent


class ChatbotNetwork:
    def __init__(self):

        self.conversation = ConversationAgent()

        self.retriever = RetrieverAgent()

        self.response = ResponseAgent()

    def chat(self, session_id, message):

        history = self.conversation.get_history(session_id)

        faq_context = self.retriever.retrieve(message)

        answer = self.response.generate_response(history, faq_context, message)

        self.conversation.save_user_message(session_id, message)

        self.conversation.save_bot_message(session_id, answer)

        return answer

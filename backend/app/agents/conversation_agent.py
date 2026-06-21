# app/agents/conversation_agent.py

from app.services.conversation_service import ConversationService


class ConversationAgent:
    def __init__(self):

        self.conversation_service = ConversationService()

    def get_history(self, session_id):
        return self.conversation_service.get_history(session_id)

    def save_user_message(self, session_id, message):
        self.conversation_service.add_message(session_id, "user", message)

    def save_bot_message(self, session_id, message):
        self.conversation_service.add_message(session_id, "assistant", message)

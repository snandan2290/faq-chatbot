from app.services.faq_service import FAQService


class RetrieverService:
    def __init__(self):
        self.faq_service = FAQService()

    def retrieve(self, question: str):

        answer = self.faq_service.find_answer(question)

        return answer

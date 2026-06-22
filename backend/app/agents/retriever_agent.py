from app.services.retriever_service import RetrieverService


class RetrieverAgent:
    def __init__(self):

        self.retriever = RetrieverService()

    def retrieve(self, question):

        return self.retriever.retrieve(question)

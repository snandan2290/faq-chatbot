import json

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


class FAQService:
    def __init__(self):

        with open("app/data/faq.json", "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.question_embeddings = self.model.encode(
            [faq["question"] for faq in self.faqs]
        )

    def find_answer(self, user_question):

        user_embedding = self.model.encode(user_question)

        similarities = cos_sim(user_embedding, self.question_embeddings)[0]

        best_index = similarities.argmax()

        score = similarities[best_index]

        if score < 0.5:
            return None

        return self.faqs[best_index]["answer"]

    def build_context(self):

        context = ""

        for faq in self.faqs:
            context += f"Q: {faq['question']}\nA: {faq['answer']}\n\n"

        return context

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
from app.agents.chatbot_network import ChatbotNetwork
from app.services.neuro_san_service import NeuroSANService

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    session_id: str
    message: str


#  Custom FAQ chatbot agent
# network = ChatbotNetwork()
# @app.post("/chat")
# async def chat(request: ChatRequest):

#     answer = network.chat(request.session_id, request.message)

#     return {"answer": answer}

neuro_san_service = NeuroSANService()


@app.post("/chat")
async def chat(request: ChatRequest):

    answer = neuro_san_service.ask(request.message)

    return {"answer": answer}

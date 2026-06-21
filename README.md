# FAQ Chatbot using Neuro-SAN

An AI-powered FAQ chatbot built using React, FastAPI, Neuro-SAN, OpenAI GPT-4o, Docker, and GitHub Actions.

---

## Project Overview

This project implements a conversational FAQ chatbot capable of answering user questions using a predefined FAQ dataset.

The chatbot leverages:

- React for the frontend UI
- FastAPI for the backend API
- Neuro-SAN for conversation orchestration
- OpenAI GPT-4o for response generation
- Docker for containerization
- GitHub Actions for CI/CD
- DockerHub for image publishing

---

## Architecture

```text
+----------------+
| React Frontend |
+----------------+
        |
        v
+----------------+
| FastAPI API    |
+----------------+
        |
        v
+----------------+
| Neuro-SAN      |
| Conversation   |
| Agent          |
+----------------+
        |
        v
+----------------+
| FAQ Dataset    |
| (faq.json)     |
+----------------+
        |
        v
+----------------+
| OpenAI GPT-4o  |
+----------------+
```

---

## Tech Stack

### Frontend

- React
- Axios
- Vite

### Backend

- FastAPI
- Python 3.12
- Neuro-SAN
- OpenAI

### AI & NLP

- Neuro-SAN
- GPT-4o
- Sentence Transformers

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- DockerHub

---

## Neuro-SAN Integration

Neuro-SAN is used as the conversational orchestration layer.

The chatbot workflow:

1. User submits a question.
2. FastAPI receives the request.
3. FAQ data is loaded from `faq.json`.
4. FAQ context is supplied to the Neuro-SAN agent.
5. Neuro-SAN invokes GPT-4o.
6. GPT-4o generates a contextual response.
7. Response is returned to the React frontend.

---

## Project Structure

```text
faq-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── services/
│   │   ├── data/
│   │   │   └── faq.json
│   │   └── main.py
│   │
│   ├── registries/
│   │   ├── manifest.hocon
│   │   └── faq_chatbot.hocon
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
│
└── .github/
    └── workflows/
        └── docker-build.yml
```

---

## Environment Variables

Create a `.env` file inside the backend directory.

```env
OPENAI_API_KEY=your_openai_api_key

AGENT_MANIFEST_FILE=./registries/manifest.hocon
```

---

## Running Locally

### Clone Repository

```bash
git clone https://github.com/snandan2290/faq-chatbot.git

cd faq-chatbot
```

---

### Backend

```bash
cd backend

python -m venv ven

ven\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Running with Docker

Build and start all services:

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000
```

Stop containers:

```bash
docker compose down
```

---

## API Endpoint

### Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "session_id": "123",
  "message": "How do I change my bank account?"
}
```

Response:

```json
{
  "answer": "You can change your registered bank account by submitting an update request."
}
```

---

## FAQ Dataset

The chatbot knowledge base is maintained in:

```text
backend/app/data/faq.json
```

Example:

```json
[
  {
    "question": "How do I change my bank account?",
    "answer": "You can change your registered bank account by submitting an update request."
  },
  {
    "question": "Is there any charge?",
    "answer": "No charge applies for updating your bank account."
  }
]
```

New FAQs can be added without changing application code.

---

## CI/CD Pipeline

GitHub Actions automatically:

1. Builds backend Docker image
2. Builds frontend Docker image
3. Pushes backend image to DockerHub
4. Pushes frontend image to DockerHub

Pipeline triggers on:

```text
Push to master branch
```

Workflow file:

```text
.github/workflows/docker-build.yml
```

---

## DockerHub Images

Backend Image:

https://hub.docker.com/r/vnandan/faq-backend

Frontend Image:

https://hub.docker.com/r/vnandan/faq-frontend

---

## Sample Questions

```text
How do I change my bank account?

Is there any charge?
```

---

## Future Enhancements

- Vector database integration
- Retrieval-Augmented Generation (RAG)
- Multi-session conversation memory
- User authentication
- AWS deployment
- Observability and monitoring
- Advanced agent workflows using Neuro-SAN

---

## Deliverables

### Application

- React Frontend
- FastAPI Backend
- Neuro-SAN Integration
- OpenAI GPT-4o Integration

### Dockerization

- Backend Dockerfile
- Frontend Dockerfile
- Docker Compose

### CI/CD

- GitHub Repository
- GitHub Actions Workflow
- DockerHub Publishing

---

## Alternative Custom Multi-Agent Implementation

In addition to the Neuro-SAN implementation, the project also includes a custom multi-agent architecture developed from scratch to demonstrate agent orchestration concepts.

### Custom Agent Architecture

```text
Conversation Agent
        |
        v
Retriever Agent
        |
        v
Response Agent
        |
        v
Groq LLM
```

### Components

#### ConversationAgent

Responsible for:

- Maintaining session context
- Managing conversation history
- Coordinating interactions between agents

#### RetrieverAgent

Responsible for:

- Retrieving relevant FAQ information
- Matching user questions against FAQ data
- Providing contextual information for response generation

#### ResponseAgent

Responsible for:

- Generating final responses
- Interacting with the Groq LLM
- Producing user-friendly answers

#### ChatbotNetwork

Responsible for:

- Orchestrating all agents
- Managing request flow
- Returning final responses to the API layer
- Switching to the Custom Agent Workflow

The application currently uses Neuro-SAN as the primary conversational engine.

To use the custom multi-agent implementation, update backend/app/main.py and uncomment:

```python
network = ChatbotNetwork()

@app.post("/chat")
async def chat(request: ChatRequest):

    answer = network.chat(
        request.session_id,
        request.message
    )

    return {"answer": answer}
```

Additional Environment Variable

#### The custom agent implementation requires a Groq API key:

```env
# Optional Custom Multi-Agent Implementation

GROQ_API_KEY=your_groq_api_key
```

### Purpose

This implementation was developed to demonstrate custom agent orchestration, retrieval, and response generation without relying on Neuro-SAN.

The Neuro-SAN implementation remains the primary solution used for assignment delivery and evaluation.

## Author

Vidyanandan S

Lead Software Engineer

GitHub:
https://github.com/snandan2290

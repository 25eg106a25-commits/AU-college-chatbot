from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot_engine import generate_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    user_message: str

@app.post("/chat")
def chat(message: Message):
    reply = generate_reply(message.user_message)
    return {"bot_reply": reply}


@app.get("/")
def home():
    return {"message": "Welcome to AU Buddy - College Assistant"}

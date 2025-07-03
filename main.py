from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
from fastapi.middleware.cors import CORSMiddleware

# Enable CORS for testing
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Simple GET to confirm root
@app.get("/")
def root():
    return {"message": "Hello from AI Boyfriend Backend!"}

# Chat request body
class ChatRequest(BaseModel):
    message: str

# POST endpoint for chat
@app.post("/chat")
async def chat(request: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a flirty AI boyfriend."},
            {"role": "user", "content": request.message}
        ]
    )
    reply = response.choices[0].message.content
    return {"response": reply}

from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Simple root check
@app.get("/")
def root():
    return {"message": "Hello from AI Boyfriend Backend!"}

# Request body model
class ChatRequest(BaseModel):
    message: str

# Chat route
@app.post("/chat")
async def chat(request: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a flirty and charming AI boyfriend."},
            {"role": "user", "content": request.message}
        ]
    )
    reply = response.choices[0].message["content"]
    return {"reply": reply}

# Uvicorn server startup for local development
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to "https://hoppscotch.io"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

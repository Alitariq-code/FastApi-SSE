from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Define the request body model
class ChatRequest(BaseModel):
    user_message: str

# Predefined responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you?": "I'm just a bot, but I'm doing great!",
    "bye": "Goodbye! Have a nice day!",
}

@router.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    user_message = request.user_message.lower()
    response = responses.get(user_message, "Sorry, I don't understand that.")
    return {"user_message": request.user_message, "bot_response": response}

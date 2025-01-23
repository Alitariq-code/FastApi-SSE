from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from time import sleep

router = APIRouter()

class ChatRequest(BaseModel):
    user_message: str

responses = {
    "hi": "Hi there! How can I assist you today?",
    "how are you?": "I'm just a bot, but I'm doing great! Thanks for asking.",
    "bye": "Goodbye! Have a wonderful day!",
}

@router.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.user_message.lower().strip()
    bot_response = responses.get(
        user_message, "Sorry, I didn't quite catch that. Could you try rephrasing?"
    )

    # Generator to stream words
    async def word_stream():
        for word in bot_response.split():
            yield f"{word} " 
            sleep(0.5) 

    return StreamingResponse(word_stream(), media_type="text/plain")

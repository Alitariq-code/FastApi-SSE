from fastapi import FastAPI
from routers import health, chat

app = FastAPI()

# Include routers
app.include_router(health.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Chatbot API"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import health, chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

# Include routers
app.include_router(health.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Chatbot API"}

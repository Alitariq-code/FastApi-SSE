
# **FastAPI Chatbot Backend**

A lightweight and scalable backend built with **FastAPI** to power a real-time chatbot application. The backend leverages **HTTP Server-Sent Events (SSE)** to stream responses word-by-word, providing a seamless and interactive user experience.

---

## **Features**
- **Real-Time Streaming**: Uses **Server-Sent Events (SSE)** to stream chatbot responses in real-time.
- **Endpoint for Chat**: A `POST` endpoint (`/api/chat`) to handle user messages and stream responses.
- **Health Check Endpoint**: A `GET` endpoint (`/api/health`) to monitor server status.
- **Extensible**: Designed to be easily extendable for integrating with AI/ML models or external APIs.

---

## **Tech Stack**
- **FastAPI**: High-performance Python web framework for building APIs.
- **StreamingResponse**: FastAPI's built-in support for SSE for efficient real-time communication.

---

## **Getting Started**

### **1. Prerequisites**
Ensure you have the following installed:
- **Python 3.9+**
- **pip** (Python package manager)

---

### **2. Clone the Repository**
```bash
git clone https://github.com/your-username/repo-name
cd fastapi-chatbot-backend
```

---

### **3. Set Up a Virtual Environment**
It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

---

### **4. Install Dependencies**
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

---

### **5. Run the Server**
Start the FastAPI server using `uvicorn`:

```bash
uvicorn app.main:app --reload
```

The server will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## **Endpoints**

### **1. Chat Endpoint**
- **URL**: `/api/chat`
- **Method**: `POST`
- **Description**: Accepts user input and streams the bot's response word-by-word using SSE.
- **Request Body (JSON)**:
  ```json
  {
    "user_message": "hello"
  }
  ```
- **Response**: Streams the bot's response as text chunks.

---

### **2. Health Check Endpoint**
- **URL**: `/api/health`
- **Method**: `GET`
- **Description**: Returns the current status of the server.
- **Response**:
  ```json
  {
    "status": "success",
    "message": "The server is up and running."
  }
  ```

---

## **How It Works**

### **Server-Sent Events (SSE)**
- The `/api/chat` endpoint streams responses using FastAPI's `StreamingResponse`.
- Each word of the bot's response is sent as a separate chunk, providing real-time updates.

### **Streaming Example**
- **Client Request**: Sends a message like `"hello"` to `/api/chat`.
- **Server Response**:
  ```
  data: Hi
  data: there!
  data: How
  data: can
  data: I
  data: help
  data: you
  data: today?
  ```

---

## **Example CURL Commands**

### **1. Test the Health Endpoint**
```bash
curl -X GET http://127.0.0.1:8000/api/health
```

### **2. Test the Chat Endpoint**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"user_message": "hello"}' \
http://127.0.0.1:8000/api/chat
```

---

## **Folder Structure**
```bash
fastapi-chatbot-backend/
├── app/
│   ├── __init__.py
│   ├── main.py          # Main application
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py    # Health endpoint
│   │   ├── chat.py      # Chat endpoint
│   ├── models/
│   │   ├── __init__.py
│   │   ├── chat.py      # Pydantic models
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## **Future Enhancements**
- **AI Integration**: Connect the chatbot to an AI/ML model like OpenAI's GPT or Hugging Face transformers.
- **Authentication**: Add API authentication for secure access.
- **Persistent Storage**: Log conversations to a database.

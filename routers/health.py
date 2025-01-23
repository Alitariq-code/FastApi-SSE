from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/health", status_code=status.HTTP_200_OK)
def health_check():
    response_data = {
        "status": "success",
        "code": 200,
        "message": "The server is up and running smoothly.",
    }
    return JSONResponse(content=response_data)

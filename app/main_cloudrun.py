from fastapi import FastAPI
from app.services.booking_service import BookingService

app = FastAPI()
service = BookingService()

@app.post("/book")
def create_booking(payload: dict):
    request_id = service.create_booking(payload)
    return {
        "status": "ACCEPTED",
        "request_id": request_id
    }

@app.get("/health")
def health():
    return {"status": "ok"}
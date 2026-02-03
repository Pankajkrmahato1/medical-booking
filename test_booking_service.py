import app.main

from app.services.booking_service import BookingService

service = BookingService()

request_id = service.create_booking({
    "name": "Pankaj",
    "gender": "MALE",
    "dob": "1997-02-03",
    "services": ["Blood Test", "X-Ray"]
})

print("Booking started with request_id:", request_id)
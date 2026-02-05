import app.main
from app.services.booking_service import BookingService

service = BookingService()

for i in range(4):
    print(f"\n--- Booking Attempt {i + 1} ---")
    request_id = service.create_booking({
        "name": "Pankaj",
        "gender": "MALE",
        "dob": "2026-02-06",
        "services": ["Blood Test", "X-Ray", "ECG"]
    })
    print("Booking started with request_id:", request_id)
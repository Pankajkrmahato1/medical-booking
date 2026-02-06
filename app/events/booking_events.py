from app.events.base import BaseEvent
import uuid

class BookingRequested:
    event_type = "BOOKING_REQUESTED"
    def __init__(self, payload: dict):
        self.request_id = str(uuid.uuid4())
        self.payload = payload

class PriceCalculated(BaseEvent):
    def __init__(self, payload, request_id):
        super().__init__("PriceCalculated", payload, request_id)

class DiscountApplied(BaseEvent):
    def __init__(self, payload, request_id):
        super().__init__("DiscountApplied", payload, request_id)

class QuotaExceeded(BaseEvent):
    def __init__(self, payload, request_id):
        super().__init__("QuotaExceeded", payload, request_id)

class BookingConfirmed(BaseEvent):
    def __init__(self, payload, request_id):
        super().__init__("BookingConfirmed", payload, request_id)

class BookingFailed(BaseEvent):
    def __init__(self, payload, request_id):
        super().__init__("BookingFailed", payload, request_id)
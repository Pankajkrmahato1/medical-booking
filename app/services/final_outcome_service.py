from app.events.event_bus import event_bus
from app.events.base import BaseEvent


class FinalOutcomeService:
    def __init__(self):
        event_bus.subscribe("QuotaApproved", self.handle_success)
        event_bus.subscribe("BookingFailed", self.handle_failure)

    def handle_success(self, event: BaseEvent):
        payload = event.payload

        print("\n✅ BOOKING CONFIRMED")
        print(f"Reference ID: {event.request_id}")
        print(f"Final Price: ₹{payload['final_price']}")
        print("-" * 40)

    def handle_failure(self, event: BaseEvent):
        payload = event.payload

        print("\n❌ BOOKING FAILED")
        print(f"Reference ID: {event.request_id}")
        print(f"Reason: {payload['reason']}")
        print("-" * 40)
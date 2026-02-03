from app.events.event_bus import event_bus
from app.events.booking_events import BookingRequested


class BookingService:
    def create_booking(self, user_data: dict):
        event = BookingRequested(payload=user_data)
        event_bus.publish(event)
        return event.request_id
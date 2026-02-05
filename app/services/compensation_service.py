from app.events.event_bus import event_bus
from app.events.base import BaseEvent


class CompensationService:
    def __init__(self):
        event_bus.subscribe("BookingRejected", self.handle_rejection)

    def handle_rejection(self, event: BaseEvent):
        reason = event.payload["reason"]

        # Emit final failure event
        event_bus.publish(
            BaseEvent(
                name="BookingFailed",
                payload={
                    "status": "FAILED",
                    "reason": reason
                },
                request_id=event.request_id
            )
        )
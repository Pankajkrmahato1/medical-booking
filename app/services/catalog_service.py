from app.events.event_bus import event_bus
from app.events.booking_events import BookingFailed
from app.events.base import BaseEvent


SERVICE_CATALOG = {
    "MALE": {
        "Blood Test": 300,
        "X-Ray": 500,
        "ECG": 400
    },
    "FEMALE": {
        "Blood Test": 300,
        "X-Ray": 500,
        "ECG": 400,
        "Pregnancy Test": 800
    }
}


class CatalogService:
    def __init__(self):
        event_bus.subscribe("BookingRequested", self.validate_services)

    def validate_services(self, event: BaseEvent):
        payload = event.payload
        gender = payload["gender"]
        selected_services = payload["services"]

        available_services = SERVICE_CATALOG.get(gender, {})

        invalid_services = [
            s for s in selected_services if s not in available_services
        ]

        if invalid_services:
            failure_event = BookingFailed(
                payload={
                    "reason": "Invalid service selection",
                    "invalid_services": invalid_services
                },
                request_id=event.request_id
            )
            event_bus.publish(failure_event)
            return

        validated_event = BaseEvent(
            name="ServiceValidationCompleted",
            payload={
                "services": selected_services,
                "prices": {
                    s: available_services[s] for s in selected_services
                }
            },
            request_id=event.request_id
        )

        event_bus.publish(validated_event)
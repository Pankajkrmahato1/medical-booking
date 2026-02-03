from app.events.event_bus import event_bus
from app.events.base import BaseEvent


class PricingService:
    def __init__(self):
        event_bus.subscribe("ServiceValidationCompleted", self.calculate_price)

    def calculate_price(self, event: BaseEvent):
        prices = event.payload["prices"]

        base_price = sum(prices.values())

        price_event = BaseEvent(
            name="PriceCalculated",
            payload={
                "services": event.payload["services"],
                "prices": prices,
                "base_price": base_price
            },
            request_id=event.request_id
        )

        event_bus.publish(price_event)
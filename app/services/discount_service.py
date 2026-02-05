from datetime import datetime

from app.events.event_bus import event_bus
from app.events.base import BaseEvent


class DiscountService:
    def __init__(self):
        # Listen for pricing completion
        event_bus.subscribe("PriceCalculated", self.apply_discount)

    def apply_discount(self, event: BaseEvent):
        payload = event.payload

        base_price = payload["base_price"]
        dob = payload.get("dob")
        gender = payload.get("gender")

        today = datetime.today().strftime("%m-%d")
        discount = 0

        # Check birthday match (month-day only)
        birthday_match = False
        if dob:
            birthday = datetime.strptime(dob, "%Y-%m-%d").strftime("%m-%d")
            birthday_match = birthday == today

       
        if (gender == "FEMALE" and birthday_match) or base_price > 1000:
            discount = round(base_price * 0.12, 2)

        final_price = base_price - discount

        discount_event = BaseEvent(
            name="DiscountApplied",
            payload={
                "base_price": base_price,
                "discount": discount,
                "final_price": final_price
            },
            request_id=event.request_id
        )

        event_bus.publish(discount_event)
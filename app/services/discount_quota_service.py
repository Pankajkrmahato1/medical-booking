from datetime import datetime

from app.events.event_bus import event_bus
from app.events.base import BaseEvent

DAILY_DISCOUNT_LIMIT = 2  


class DiscountQuotaService:
    def __init__(self):
        self.current_date = self._today()
        self.used_discounts = 0

        event_bus.subscribe("DiscountApplied", self.check_quota)

    def _today(self):
        return datetime.now().strftime("%Y-%m-%d")

    def _reset_if_new_day(self):
        today = self._today()
        if today != self.current_date:
            self.current_date = today
            self.used_discounts = 0

    def check_quota(self, event: BaseEvent):
        self._reset_if_new_day()

        payload = event.payload
        discount = payload["discount"]

        # Only count R1 discounts
        if discount > 0:
            if self.used_discounts >= DAILY_DISCOUNT_LIMIT:
                # Reject booking
                event_bus.publish(
                    BaseEvent(
                        name="BookingRejected",
                        payload={
                            "reason": "Daily discount quota reached. Please try again tomorrow."
                        },
                        request_id=event.request_id
                    )
                )
                return

            self.used_discounts += 1

        event_bus.publish(
            BaseEvent(
                name="QuotaApproved",
                payload=payload,
                request_id=event.request_id
            )
        )
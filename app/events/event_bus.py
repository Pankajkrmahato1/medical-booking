import json
import os
import logging
from google.cloud import pubsub_v1

# --------------------------------------------------
# Configuration
# --------------------------------------------------

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
if not PROJECT_ID:
    raise RuntimeError("GCP_PROJECT_ID environment variable is not set")

TOPIC_NAME = os.getenv("BOOKING_EVENTS_TOPIC", "booking-events")

# --------------------------------------------------
# Pub/Sub setup
# --------------------------------------------------

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EventBus:
    def publish(self, event):
        """
        Publish a domain event to Google Pub/Sub.
        This blocks on publish to surface failures explicitly.
        """

        message = {
            "event_type": event.event_type,
            "request_id": event.request_id,
            "payload": event.payload,
        }

        data = json.dumps(message).encode("utf-8")

        logger.info(
            "📤 Publishing event=%s request_id=%s topic=%s",
            event.event_type,
            event.request_id,
            topic_path,
        )

        try:
            future = publisher.publish(topic_path, data)
            message_id = future.result()  # IMPORTANT: force error if publish fails

            logger.info(
                "✅ Event published successfully message_id=%s request_id=%s",
                message_id,
                event.request_id,
            )

        except Exception as exc:
            logger.exception(
                "❌ Failed to publish event=%s request_id=%s",
                event.event_type,
                event.request_id,
            )
            raise exc


# Singleton instance
event_bus = EventBus()
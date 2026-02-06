import json
import os
from google.cloud import pubsub_v1

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "medical-booking-system-486523")

publisher = pubsub_v1.PublisherClient()


def publish_event(topic: str, message: dict):
    topic_path = publisher.topic_path(PROJECT_ID, topic)

    data = json.dumps(message).encode("utf-8")

    future = publisher.publish(topic_path, data=data)
    future.result()  
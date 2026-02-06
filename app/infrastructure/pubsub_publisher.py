from google.cloud import pubsub_v1
import json
import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
publisher = pubsub_v1.PublisherClient()

def publish_event(topic: str, payload: dict):
    topic_path = publisher.topic_path(PROJECT_ID, topic)
    data = json.dumps(payload).encode("utf-8")
    publisher.publish(topic_path, data)
from google.cloud import pubsub_v1
import json
from app.services.validation_service import ValidationService
from app.infrastructure.pubsub_publisher import publish_event
import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
SUBSCRIPTION = "booking-validator-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION)

def callback(message):
    data = json.loads(message.data)
    request_id = data["request_id"]
    payload = data["payload"]

    service = ValidationService()
    prices = service.validate(payload)

    publish_event("booking-validated", {
        "request_id": request_id,
        "prices": prices
    })

    message.ack()

subscriber.subscribe(subscription_path, callback=callback)
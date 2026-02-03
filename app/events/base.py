from datetime import datetime
from uuid import uuid4

class BaseEvent:
    def __init__(self, name: str, payload: dict, request_id: str = None):
        self.name = name
        self.payload = payload
        self.request_id = request_id or str(uuid4())
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return {
            "event": self.name,
            "request_id": self.request_id,
            "timestamp": self.timestamp.isoformat(),
            "payload": self.payload
        }
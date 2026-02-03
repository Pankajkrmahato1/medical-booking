import json
from datetime import datetime

def log_event(event):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "request_id": event.request_id,
        "event": event.name,
        "payload": event.payload
    }
    print(json.dumps(log))
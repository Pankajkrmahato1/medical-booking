from collections import defaultdict
from typing import Callable, Dict, List
from app.logging.logger import log_event


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)

    def subscribe(self, event_name: str, handler: Callable):
        self.subscribers[event_name].append(handler)

    def publish(self, event):
        log_event(event)
        handlers = self.subscribers.get(event.name, [])
        for handler in handlers:
            handler(event)


event_bus = EventBus()
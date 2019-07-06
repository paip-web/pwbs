from pwbs.core.event_sourcing.event_handler import EventHandler
from pwbs.core.exceptions.event_handle_not_implemented import EventHandleNotImplemented
from pwbs.core.event_sourcing.event import Event
from pwbs.core.event_sourcing.event_bus import EventBus
from typing import List
from uuid import uuid4
from datetime import datetime
import time

class OrderEventHandler(EventHandler):
    def on(self):
        raise EventHandleNotImplemented('on method not supported')

    def on_order_placed(self, current_event: Event, queue_name: str, event_queue: List[Event], event_bus: EventBus):
        event_bus.emit(queue_name, Event('order_accepted', {
            "id": uuid4(),
        }))
        del current_event[[event_bus, queue_name]]

    def on_order_accepted(self, current_event: Event, queue_name: str, event_queue: List[Event], event_bus: EventBus):
        time.sleep(5)
        event_bus.emit(queue_name, Event('order_done', {
            "id": current_event.data["id"],
        }))
        del current_event[[event_bus, queue_name]]

    def on_order_done(self, current_event: Event, queue_name: str, event_queue: List[Event], event_bus: EventBus):
        event_bus.emit('analytics', Event('add_event', {
            "id": uuid4(),
            "type": "order",
            "date": datetime.now(),
        }))
        del current_event[[event_bus, queue_name]]

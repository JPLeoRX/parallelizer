import threading
from typing import Dict, Any
from simplestr import gen_str_repr


@gen_str_repr
class ExecutorEvent:
    def __init__(self, worker_index: int, event: threading.Event, return_dict: Dict) -> None:
        self.worker_index = worker_index
        self.event = event
        self.return_dict = return_dict
        self.results = None

    def save_results(self, results: Any) -> None:
        self.results = results
        if self.return_dict is not None:
            self.return_dict[self.worker_index] = results
        if self.event is not None:
            self.event.set()
        return

    def wait(self, timeout_in_seconds: float) -> None:
        if self.event is not None:
            self.event.wait(timeout_in_seconds)
        return

import threading
from simplestr import gen_str_repr


@gen_str_repr
class ExecutorEvent():
    def __init__(self, worker_index: int, event: threading.Event) -> None:
        self.worker_index = worker_index
        self.event = event
        self.results = None

import threading
from typing import List
from parallelizer.executor import Executor
from parallelizer.executor_event import ExecutorEvent
from parallelizer.parallelizer import Parallelizer


class ThreadParallelizer(Parallelizer):
    def __init__(self, number_of_threads: int, timeout_in_seconds: float = 60):
        super().__init__(number_of_threads, timeout_in_seconds)

    def start_executors(self, executors: List[Executor]) -> List[ExecutorEvent]:
        # Start threads
        executor_events = []
        for executor in executors:
            event = threading.Event()
            executor_event = ExecutorEvent(executor.worker_index, event, None)
            executor_events.append(executor_event)
            thread = threading.Thread(target=executor.execute_all, args=[executor_event])
            thread.start()

        # Return events
        return executor_events

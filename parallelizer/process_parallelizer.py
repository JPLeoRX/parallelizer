import multiprocessing
from typing import List
from parallelizer.executor import Executor
from parallelizer.executor_event import ExecutorEvent
from parallelizer.parallelizer import Parallelizer


class ProcessParallelizer(Parallelizer):
    def __init__(self, number_of_threads: int, timeout_in_seconds: float = 60):
        super().__init__(number_of_threads, timeout_in_seconds)

    def start_executors(self, executors: List[Executor]) -> List[ExecutorEvent]:
        # Keep return values in a memory-shared dict
        return_dict = multiprocessing.Manager().dict()

        # Start processes
        executor_events = []
        processes = []
        for executor in executors:
            executor_event = ExecutorEvent(executor.worker_index, None, return_dict)
            executor_events.append(executor_event)
            process = multiprocessing.Process(target=executor.execute_all, args=[executor_event])
            processes.append(process)
            process.start()

        # Wait for all processes to finish
        for process in processes:
            process.join(self.timeout_in_seconds)

        # Map results back from shared dict into each event
        for executor_event in executor_events:
            executor_event.results = return_dict[executor_event.worker_index]

        # Return events
        return executor_events

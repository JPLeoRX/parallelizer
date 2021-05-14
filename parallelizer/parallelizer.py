import math
from typing import Callable, Any, List

from parallelizer.executor import Executor
from parallelizer.executor_event import ExecutorEvent
from parallelizer.task import Task


class Parallelizer:
    def __init__(self, number_of_threads: int, timeout_in_seconds: float = 60):
        if number_of_threads <= 0:
            raise ValueError('Number of threads cannot be less than or equal to zero. Use minimum 1 thread.')
        self.number_of_threads = number_of_threads
        if timeout_in_seconds <= 0:
            raise ValueError('Timeout cannot be less than or equal to zero seconds.')
        self.timeout_in_seconds = timeout_in_seconds

    def execute(self, method: Callable, arguments: List[List[Any]]) -> List[Any]:
        # Sanity checks of inputs
        if len(arguments) == 0:
            raise ValueError("Arguments list can't be empty")
        number_of_tasks = len(arguments[0])
        for inner_arguments in arguments:
            if len(inner_arguments) != number_of_tasks:
                raise ValueError("Inner arguments list are not all of the same length! arguments=" + str(arguments))

        # Build tasks
        tasks = self._build_tasks(method, arguments)

        # Split tasks by threads
        tasks_by_threads = self._split_list_by_number_of_chunks(tasks, self.number_of_threads)

        # Build executors
        executors = self._build_executors(tasks_by_threads)

        # Start executors
        executor_events = self.start_executors(executors)

        # Wait for executors to finish
        results = []
        for executor_event in executor_events:
            executor_event.wait(self.timeout_in_seconds)
            results.extend(executor_event.results)

        # Resort results to keep submission order
        results = sorted(results, key = lambda r: r.task_index)

        # Map back to return values
        return [r.result for r in results]

    def start_executors(self, executors: List[Executor]) -> List[ExecutorEvent]:
        pass

    def _build_tasks(self, method: Callable, arguments: List[List[Any]]) -> List[Task]:
        tasks = []
        number_of_tasks = len(arguments[0])
        for task_index in range(0, number_of_tasks):
            task_method_arguments = []
            for inner_arguments in arguments:
                task_method_arguments.append(inner_arguments[task_index])
            task = Task(task_index, method, task_method_arguments)
            tasks.append(task)
        return tasks

    def _build_executors(self, tasks_by_threads: List[List[Task]]) -> List[Executor]:
        executors = []
        for worker_index in range(0, len(tasks_by_threads)):
            executors.append(Executor(worker_index, tasks_by_threads[worker_index]))
        return executors

    def _split_list_by_size_of_chunk(self, list: List[Any], size_of_chunk: int) -> List[List[Any]]:
        chunks = []
        for i in range(0, len(list), size_of_chunk):
            chunks.append(list[i:i + size_of_chunk])
        return chunks

    def _split_list_by_number_of_chunks(self, list: List[Any], number_of_chunks: int) -> List[List[Any]]:
        size_of_chunk = int(math.ceil(len(list) / number_of_chunks))
        return self._split_list_by_size_of_chunk(list, size_of_chunk)

from typing import List

from parallelizer.executor_event import ExecutorEvent
from parallelizer.result import Result
from parallelizer.task import Task


class Executor:
    def __init__(self, worker_index: int, tasks: List[Task]):
        self.worker_index = worker_index
        self.tasks = tasks

    def execute_all(self, executor_event: ExecutorEvent) -> List[Result]:
        results = []
        for task in self.tasks:
            results.append(self._execute_single(task))
        executor_event.save_results(results)
        return results

    def _execute_single(self, task: Task) -> Result:
        return Result(task.task_index, task.execute())

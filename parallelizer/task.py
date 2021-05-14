from typing import Any, List, Callable
from simplestr import gen_str_repr


@gen_str_repr
class Task:
    def __init__(self, task_index: int, method: Callable, method_arguments: List[Any]):
        self.task_index = task_index
        self.method = method
        self.method_arguments = method_arguments

    def execute(self) -> Any:
        return self.method(*self.method_arguments)

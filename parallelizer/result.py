from typing import Any
from simplestr import gen_str_repr


@gen_str_repr
class Result:
    def __init__(self, task_index: int, result: Any):
        self.task_index = task_index
        self.result = result

from typing import Any, List


def repeat(value: Any, number_of_times: int) -> List[Any]:
    result = []
    for i in range(0, number_of_times):
        result.append(value)
    return result

import time
from typing import List

from parallelizer.thread_parallelizer import ThreadParallelizer
from parallelizer.process_parallelizer import ProcessParallelizer
from parallelizer.tools import repeat


def power_function(base: int, power: int) -> List[int]:
    time.sleep(1)
    return [base, base ** power]


inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_of_workers = 5


def test_thread_parallelizer():
    t1 = time.time()
    prlz = ThreadParallelizer(number_of_workers)
    results = prlz.execute(power_function, [inputs, repeat(2, len(inputs))])
    t2 = time.time()
    print(inputs)
    print(results)
    print('test_thread_parallelizer(): Execution time:', t2 - t1)


def test_process_parallelizer():
    t1 = time.time()
    prlz = ProcessParallelizer(number_of_workers)
    results = prlz.execute(power_function, [inputs, repeat(2, len(inputs))])
    t2 = time.time()
    print(inputs)
    print(results)
    print('test_process_parallelizer(): Execution time:', t2 - t1)


test_thread_parallelizer()
test_process_parallelizer()
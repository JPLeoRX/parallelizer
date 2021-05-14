import time
from parallelizer.thread_parallelizer import ThreadParallelizer
from parallelizer.process_parallelizer import ProcessParallelizer
from parallelizer.tools import repeat


def cpu_load(index: int) -> int:
    for x in range(0, 3000):
        y = x ** x
    return index


inputs = list(range(0, 10))
number_of_workers = 10


def test_thread_parallelizer():
    t1 = time.time()
    prlz = ThreadParallelizer(number_of_workers)
    results = prlz.execute(cpu_load, [inputs])
    t2 = time.time()
    print(inputs)
    print(results)
    print('test_thread_parallelizer(): Execution time:', t2 - t1)


def test_process_parallelizer():
    t1 = time.time()
    prlz = ProcessParallelizer(number_of_workers)
    results = prlz.execute(cpu_load, [inputs])
    t2 = time.time()
    print(inputs)
    print(results)
    print('test_process_parallelizer(): Execution time:', t2 - t1)


test_thread_parallelizer()
test_process_parallelizer()

# This test demonstrates that for tasks that load CPU we should use the process executor
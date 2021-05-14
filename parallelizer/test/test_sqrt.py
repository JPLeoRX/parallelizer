import time
from parallelizer.thread_parallelizer import ThreadParallelizer
from parallelizer.process_parallelizer import ProcessParallelizer


def power_function(base: int, power: int) -> int:
    time.sleep(1)
    return base ** power

inputs = list(range(1, 11))

# Test threads
t1 = time.time()
prlz = ThreadParallelizer(10)
results = prlz.execute(power_function, [inputs, [2 for i in inputs]])
t2 = time.time()
print(inputs)
print(results)
print('Execution time:', t2 - t1)

# Test process
t1 = time.time()
prlz = ProcessParallelizer(10)
results = prlz.execute(power_function, [inputs, [2 for i in inputs]])
t2 = time.time()
print(inputs)
print(results)
print('Execution time:', t2 - t1)
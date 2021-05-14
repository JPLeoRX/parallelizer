import time
from parallelizer import ThreadParallelizer, ProcessParallelizer, repeat

def power_function(base: int, power: int) -> int:
    time.sleep(1)
    return base ** power

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_of_threads = 5

thread_parallelizer = ThreadParallelizer(number_of_threads)
results = thread_parallelizer.execute(power_function, [inputs, repeat(2, len(inputs))])
print(inputs)
print(results)

process_parallelizer = ProcessParallelizer(number_of_threads)
results = process_parallelizer.execute(power_function, [inputs, repeat(2, len(inputs))])
print(inputs)
print(results)
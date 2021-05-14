from parallelizer.thread_parallelizer import ThreadParallelizer


def power_function(base: int, power: int) -> int:
    return base ** power

inputs = list(range(1, 11))
prlz = ThreadParallelizer(4)
results = prlz.execute(power_function, [inputs, [2 for i in inputs]])

print(inputs)
print(results)
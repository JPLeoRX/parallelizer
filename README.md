# parallelizer
Parallel execution of your tasks simplified! This package can be used as an alternative to Python's `concurrent.futures` executors, or as an analog of Java's `ExecutorService`.

Two simple wrappers (thread-based and process-based), that allow for easy split and parallel processing of your jobs.

# Description
This package provides two classes:
- `ThreadParallelizer` to execute your jobs in new threads
- `ProcessParallelizer` to execute your jobs in new processes

This is a pure python implementation, with usage of `threading` and `multiprocessing` packages

Note that the wrappers appear to be in sync (from the caller's perspective), they will wait until all inner tasks are completed. 

# Installation
 
## Normal installation

```bash
pip install parallelizer
```

## Development installation

```bash
git clone https://github.com/jpleorx/parallelizer.git
cd parallelizer
pip install --editable .
```

# Example
```python
import time
from parallelizer import ThreadParallelizer, ProcessParallelizer, repeat

def power_function(base: int, power: int) -> int:
    time.sleep(1)
    return base ** power

inputs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number_of_threads = 5

thread_parallelizer = ThreadParallelizer(number_of_threads)
results = thread_parallelizer.execute(power_function, [inputs, repeat(2, len(inputs))])

process_parallelizer = ProcessParallelizer(number_of_threads)
results = process_parallelizer.execute(power_function, [inputs, repeat(2, len(inputs))])
```
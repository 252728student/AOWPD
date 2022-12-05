import numpy as np
import cupy as cp
from cupyx.profiler import benchmark
import cupyx.profiler as profiler

from SitoGPU import sito

def main():
    N = 100000
    data_array = cp.asarray(np.ones(N+1, dtype=int))
    data_array[0] = 0
    data_array[1] = 0
    kernel = sito()
    with profiler.profile():
        print(benchmark(kernel, (((N+1+255)//1024,), (1024,),(data_array, N+1)), n_repeat=10))
    """
     for index, elem in enumerate(cp.asnumpy(data_array)):
            if elem:
            print(index, end= ", ")
    """
if __name__ == "__main__":
    main()
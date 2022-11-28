import numpy as np
import cupy as cp
from cupyx.profiler import benchmark

from SitoGPU import sito

def main():
    print("Input N:")
    N = int(input())
    data_array = cp.asarray(np.ones(N+1, dtype=int))
    data_array[0] = 0
    data_array[1] = 0
    kernel = sito()
    print(benchmark(kernel, (((N+1+255)//256,), (256,),(data_array, N+1))))
    """
     for index, elem in enumerate(cp.asnumpy(data_array)):
            if elem:
            print(index, end= ", ")
    """
    return

if __name__ == "__main__":
    main()
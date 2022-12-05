import numpy as np
import cupy as cp
from cupyx.profiler import benchmark
import cupyx.profiler as profiler

from SitoGPU import sito
from Sito2 import sito2

def main():
    N = 10000
    data_array= cp.asarray(np.ones(N*(N+1), dtype=int))
    cp.reshape(data_array, [N+1, N]);
  #  kernel = sito()
    kernel = sito2()
    with profiler.profile():
        print(benchmark(kernel, (((N+1+1023)//1024 + 1,), (1024,),(data_array, N+1)), n_repeat=10))

    """
     for index, elem in enumerate(cp.asnumpy(data_array)):
            if elem:
            print(index, end= ", ")
    """
    """
    OOF_DATA = cp.asnumpy(data_array)
    RESULT = np.ones(N+1, dtype=int)
    RESULT[0] = 0
    RESULT[1] = 0
    for i, elem in enumerate(OOF_DATA):
            if(elem == 0):
                RESULT[i%(N+1)] = 0
    for index, elem in enumerate(RESULT):
        if elem:
            print(index, end=", ")
    """
if __name__ == "__main__":
    main()
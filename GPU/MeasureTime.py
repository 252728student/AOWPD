import numpy as np
import cupy as cp
from time import time

from SitoGPU import sito

def main():
    print("Input N:")
    N = int(input())
    data_array = cp.asarray(np.ones(N+1, dtype=int))
    data_array[0] = 0;
    data_array[1] = 0;
    kernel = sito()
    kernel((1,), (1,), (cp.asarray([1]), 1))
    time_begin = time()
    kernel((1,), (N+1,), (data_array, N+1))
    cp.cuda.Stream.null.synchronize()
    time_end = time()
    print(time_end - time_begin)
    return

if __name__ == "__main__":
    main()
import cupy as cp

def sito():
    myKernel = cp.RawKernel(r'''
    extern "C" __global__
    void erato(int* A, int N){
        int index = threadIdx.x;
        if(index >= 2) {
            for(int i = index*index; i < N; i += index) {
                A[i] = 0;
            }
        } 
        return;
    }
    ''', 'erato')
    return myKernel

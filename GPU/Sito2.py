import cupy as cp

def sito2():
    myKernel = cp.RawKernel(r'''
    extern "C" __global__
    void erato(int* A, int N){
        int index = threadIdx.x + blockDim.x * threadIdx.y;
        if(index >= 2) {
            for(int i = index*index; i < N; i += index) {
                A[index*N + i] = 0;
            }
        } 
        return;
    }
    ''', 'erato')
    return myKernel

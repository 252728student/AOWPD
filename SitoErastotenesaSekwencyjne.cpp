#include <iostream>
#include <omp.h>
#include <chrono>
#include <thread>
#include <vector>


using namespace std;

#define LASTNUMBER 10

char* isPrime = new char[LASTNUMBER + 1];

int primes = 0;

int erato()
{
    omp_set_num_threads(omp_get_max_threads());
    int lastNumberSqrt = (int)sqrt((double)LASTNUMBER);

    //inicjalizacja
#pragma omp parallel for
    for (int i = 0; i <= LASTNUMBER; i++)
    {
        isPrime[i] = 1;
    }

    // szukanie liczb będocych nie pierwszymi
#pragma omp parallel for schedule(dynamic)
    for (int i = 2; i <= lastNumberSqrt; i++)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j <= LASTNUMBER; j += i)
            {
                isPrime[j] = 0;
            }
        }
    }

    // liczenie ilości liczb pierwszych
#pragma omp parallel for reduction(+:primes)
    for (int i = 2; i <= LASTNUMBER; i++)
    {
        primes += isPrime[i];
        if (isPrime[i])
        {
            cout << i << ",";
        }
    }
    cout << endl;

    return primes;
}

int main()
{
    int primesFound;

    auto start = chrono::steady_clock::now();
    primesFound = erato();
    auto end = chrono::steady_clock::now();

    cout << "znaleziono: " << primesFound << " liczb pierwszych" << endl;

    float time = chrono::duration_cast<chrono::nanoseconds>(end - start).count();

    cout << "Time in ns: " << time << endl;
    cout << "Time in s: " << time / 1000000000;
}




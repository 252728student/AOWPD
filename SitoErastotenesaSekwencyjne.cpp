#include <iostream>
#include <omp.h>
#include <chrono>
#include <thread>
#include <vector>


using namespace std;

#define LASTNUMBER 10000
#define REPEAT 100

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
 //       if (isPrime[i])
 //       {
 //           cout << i << ",";
 //       }
    }
//   cout << endl;

    return primes;
}

int main()
{
    int primesFound;

    float avgTime = 0;
    float timesTab[REPEAT];
    auto start = chrono::steady_clock::now();
    auto end = chrono::steady_clock::now();

   
   for (int i = 0; i < REPEAT; i++)
   {
       start = chrono::steady_clock::now();

       primesFound = erato();

       end = chrono::steady_clock::now();

       timesTab[i] = chrono::duration_cast<chrono::microseconds>(end - start).count();
   }

   for (int i = 0; i < REPEAT; i++)
   {
       avgTime += timesTab[i];
   }

    avgTime = avgTime / REPEAT;

    cout << "znaleziono: " << primesFound << " liczb pierwszych" << endl;

    cout << "Time in micro s: " << avgTime << endl;
}






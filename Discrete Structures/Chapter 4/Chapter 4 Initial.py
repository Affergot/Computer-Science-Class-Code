'''
Write a program: Write a program to count the number of primes less than some number.
Make a log plot of the number of primes less than ten, one hundred, a thousand, ten thousand,
a hundred thousand and a million. Predict the number of primes less than 10 million
'''
from math import isqrt
import time



def PrimesLessThan(target) -> list[int]:
    if target <= 2:
        return []
    is_prime = [True] * target
    is_prime[0] = False
    is_prime[1] = False

    upperlimit = isqrt(target) + 1

    for number in range(2, upperlimit):
        if is_prime[number]:
            for x in range(number * number, target, number):
                is_prime[x] = False

    return [number for number in range(target) if is_prime[number]]


if __name__ == "__main__":
    target = 10_000_000
    StartTime = time.perf_counter()
    print(len(PrimesLessThan(target)))
    TotalTime = time.perf_counter() - StartTime
    print(f"Done in {TotalTime:.2f}s")
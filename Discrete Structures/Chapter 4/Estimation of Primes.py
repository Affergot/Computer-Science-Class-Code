from math import log
import time

def EstimatedPrimesBelow(target: int) -> int:
    return target/log(target)

if __name__ == "__main__":

    target = int(input("Enter the number you would like estimated how many primes are below it\n"))

    StartTime = time.perf_counter()
    print(f"There are about {EstimatedPrimesBelow(target):,.0f} prime numbers before {target:,}")
    TotalTime = time.perf_counter() - StartTime

    if str(f"{TotalTime/1000:.4f}") == "0.0000":
        print(f"Done in {TotalTime/1000:.8f} milliseconds")
    else:
        print(f"Done in {TotalTime/1000:.4f} milliseconds")
from bisect import bisect_right
import numpy as np

def smallest_multiple_of_n_geq_m(n: int, m: int) -> int:
    return m + -m % n


class PrimeArray:
    def __init__(self, dtype=np.uint64):
        self.primes: np.ndarray = np.array([2, 3, 5, 7], dtype=dtype)
        self.end_segment: int = 1
        self.dtype = dtype
        self.extend_at_most_n_segments_target: int = 100

    def _extend_at_most_n_segments(self, n: int) -> None:
        k = self.end_segment
        n = min(n, len(self.primes) - 1 - k)
        p, q = int(self.primes[k]), int(self.primes[k + n])
        segment_min, segment_max = p * p, q * q - 1

        segment_len = segment_max - segment_min + 1
        is_prime = np.full(shape=segment_len, fill_value=True, dtype=bool)

        for pk in self.primes[:k + n]:
            pk = int(pk)
            start = smallest_multiple_of_n_geq_m(pk, segment_min)
            is_prime[start - segment_min::pk] = False

        segment = np.arange(p * p, q * q, dtype=self.dtype)
        new_primes = segment[is_prime]
        try:
            old_len = len(self.primes)
            self.primes.resize(old_len + len(new_primes))
            self.primes[old_len:] = new_primes
        except ValueError:
            self.primes = np.concatenate((self.primes, new_primes))

        self.end_segment += n

    def _extend(self) -> None:
        self._extend_at_most_n_segments(self.extend_at_most_n_segments_target)

    def CountPrimesLessOrEqual(self, n: int) -> int:
        while self.primes[-1] < n:
            self._extend()
        return bisect_right(self.primes, n)



def main():
    import time
    Target = 10_000_000
    StartTime = time.perf_counter()
    Euclid = PrimeArray()
    print(Euclid.CountPrimesLessOrEqual(Target))
    TotalTime = time.perf_counter() - StartTime
    print(f"Done in {TotalTime:.2f}s")

main()
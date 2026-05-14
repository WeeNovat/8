import multiprocessing
import time
import os

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def sum_primes_in_range(start: int, end: int) -> tuple:
    primes = [n for n in range(start, end) if is_prime(n)]
    return (sum(primes), len(primes), os.getpid())

def main():
    total_range = 500_000
    num_workers = 4
    chunk = total_range // num_workers
    ranges = [(i*chunk, (i+1)*chunk) for i in range(num_workers)]

    with multiprocessing.Pool(num_workers) as pool:
        start_time = time.perf_counter()
        results = pool.starmap(sum_primes_in_range, ranges)
        par_time = time.perf_counter() - start_time

    for i, (res_sum, count, pid) in enumerate(results):
        print(f"Worker {i} (PID {pid}): знайдено {count} чисел")

    print(f"Паралельне виконання за {num_workers} процеси: {par_time:.3f} сек")

if __name__ == "__main__": main()

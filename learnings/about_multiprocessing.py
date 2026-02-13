import time
import multiprocessing

def cpu_heavy_task(n):
    total = 0
    for i in range(10_000_000):
        total += i * n
    return total

if __name__ == "__main__":
    start = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(cpu_heavy_task, [1, 2, 3, 4])

    end = time.time()

    print("Multiprocessing Time:", end - start)

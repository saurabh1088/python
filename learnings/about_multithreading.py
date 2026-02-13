import time
from concurrent.futures import ThreadPoolExecutor

def cpu_heavy_task(n):
    total = 0
    for i in range(10_000_000):
        total += i * n
    return total

if __name__ == "__main__":
    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_heavy_task, [1, 2, 3, 4]))

    end = time.time()

    print("Threading Time:", end - start)


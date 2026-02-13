from concurrent.futures import ThreadPoolExecutor

def square(n):
    print(f"Processing {n}")
    return n * n

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, [1, 2, 3, 4, 5]))

    print(results)

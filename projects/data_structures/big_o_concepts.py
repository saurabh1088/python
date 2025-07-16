import random
import time

def example_one(n):
    for i in range(n):
        print(i)

def example_two(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

def example_three(n):
    for i in range(n):
        print(i)
        for j in range(n):
            print(i,j)

def example_big_o_one():
    start_time = time.time()

    large_list = list(range(10_000_000))
    random_index = random.randint(0, len(large_list) - 1)
    print(large_list[random_index])

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution Time: {elapsed_time:.6f} seconds")
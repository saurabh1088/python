import random
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


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
    logging.info('--- Executing example_big_o_one ---')
    start_time = time.time()

    large_list = list(range(10_000_000))
    random_index = random.randint(0, len(large_list) - 1)
    print(large_list[random_index])

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Execution Time: {elapsed_time:.6f} seconds")
    logging.info('----------------------------------------------')

def example_big_o_n():
    logging.info('--- Executing example_big_o_n ---')
    start_time = time.time()

    large_list = list(range(10_000_000))
    for number in large_list:
        print(number)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Execution Time: {elapsed_time:.6f} seconds")
    logging.info('----------------------------------------------')

def example_big_o_n_square():
    logging.info('--- Executing example_big_o_n_square ---')
    start_time = time.time()

    large_list = list(range(1000))
    for i in large_list:
        for j in large_list:
            print(i,j)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f"Execution Time: {elapsed_time:.6f} seconds")
    logging.info('----------------------------------------------')



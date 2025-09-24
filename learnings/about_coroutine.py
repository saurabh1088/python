import asyncio
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


async def an_async_function_showing_coroutine():
    """
    An example asynchronous function demonstrating the concept of coroutines in Python.

    This function prints messages to indicate its execution flow, simulates asynchronous work
    by awaiting `asyncio.sleep(10)`, and resumes execution after the sleep period. It showcases
    how coroutines can be paused and resumed using the `await` keyword, allowing other tasks
    to run concurrently during the waiting period.

    Coroutines are a fundamental building block for asynchronous programming in Python,
    enabling non-blocking operations and efficient concurrency.

    Usage:

        asyncio.run(an_async_function_showing_coroutine())
    """
    logging.info("This is an async function")
    logging.info("Simulating some async work with asyncio.sleep")
    logging.info("Sleeping...")
    await asyncio.sleep(10)
    logging.info("Waking up...")
    logging.info("Async function is done")

async def say_hello_to(person, delay=1):
    logging.info(f"Task for '{person}' started. Will wait for {delay} seconds, then will say hello.")
    logging.info(f"Hello, {person}!")
    await asyncio.sleep(delay)
    logging.info(f"Goodbye, {person}!")

async def say_hello_to_and_hear_back(person, delay=1):
    logging.info(f"Task for '{person}' started. Will wait for {delay} seconds, then will say hello.")
    greeting = f"Hello, {person}!"
    logging.info(greeting)
    await asyncio.sleep(delay)
    logging.info(f"Task for '{person}' is done.")
    return greeting

async def run_multiple_hello_tasks():
    logging.info("Starting concurrent tasks...")
    # `asyncio.gather` runs the tasks concurrently. The event loop
    # will not wait for one to finish before starting the next.
    await asyncio.gather(
        say_hello_to("Alice", 5),
        say_hello_to("Bob", 3),
        say_hello_to("Charlie", 1)
    )
    logging.info("All tasks finished.")

async def run_multiple_hello_and_hear_back_tasks():
    logging.info("Starting concurrent tasks with return values...")
    tasks = [
        say_hello_to_and_hear_back("Alice", 5),
        say_hello_to_and_hear_back("Bob", 3),
        say_hello_to_and_hear_back("Charlie", 1)
    ]
    logging.info("All tasks finished.")
    results = await asyncio.gather(*tasks)
    for result in results:
        logging.info(f"Greeting received: {result}")

if __name__ == "__main__":
    asyncio.run(run_multiple_hello_and_hear_back_tasks())

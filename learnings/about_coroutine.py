import asyncio


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
    print("This is an async function")
    print("Simulating some async work with asyncio.sleep")
    print("Sleeping...")
    await asyncio.sleep(10)
    print("Waking up...")
    print("Async function is done")

async def say_hello_to(person, delay=1):
    print(f"Task for '{person}' started. Will wait for {delay} seconds, then will say hello.")
    print(f"Hello, {person}!")
    await asyncio.sleep(delay)
    print(f"Goodbye, {person}!")

async def run_multiple_hello_tasks():
    print("Starting concurrent tasks...")
    await asyncio.gather(
        say_hello_to("Alice", 2),
        say_hello_to("Bob", 3),
        say_hello_to("Charlie", 1)
    )
    print("All tasks finished.")

if __name__ == "__main__":
    asyncio.run(run_multiple_hello_tasks())

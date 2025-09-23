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

if __name__ == "__main__":
    asyncio.run(an_async_function_showing_coroutine())

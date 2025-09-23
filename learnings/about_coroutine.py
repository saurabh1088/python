import asyncio

async def an_async_function_showing_coroutine():
    print("This is an async function")
    print("Simulating some async work with asyncio.sleep")
    print("Sleeping...")
    await asyncio.sleep(10)
    print("Waking up...")
    print("Async function is done")

if __name__ == "__main__":
    asyncio.run(an_async_function_showing_coroutine())

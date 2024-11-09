"""
asyncio
    - async/await
    - asyncio.run() - to run the main function
    - asyncio.create_task() - to run a task concurrently
    - asyncio.gather(fun,fun2,) - to run multiple tasks concurrently
    asyncio.wait_for(func, timeout) - to wait for a function to finish
event loop

aiohttp (asyncio http client)

"""

import asyncio


def func11():
    print("Function 11 started..")
    print("Function 11 Ended")
    return 1


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")
    return 1


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")
    return 2


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    func11()
    print("Function 3 Ended")
    return 3


async def main():
    L = await asyncio.gather(
        func2(),
        func1(),
        func3(),
    )
    print("Main Ended..")
    print(L)


# async def long_operation(n):
#     print(f"Starting operation {n}")
#     await asyncio.sleep(n)
#     print(f"Finished operation {n}")
#     return n


# async def main():
#     task2 = asyncio.create_task(long_operation(4))
#     task1 = asyncio.create_task(long_operation(2))
#     n = await task1 # here we are waiting for task1 to finish
#     f = await task2 # here we are waiting for task2 to finish
#     print(f"Result of task1: {n}")
#     print(f"Result of task2: {f}")
#     print("After await")


if __name__ == "__main__":
    asyncio.run(main())

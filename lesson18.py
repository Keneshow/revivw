# async def say_hello():
#     print('hello world!!')
#
import asyncio


#
# import asyncio
#
#
# async def hello():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#
#
# asyncio.run(hello())

# import asyncio
# import time
#
#
# async def coro(tag, delay):
#     t0 = time.perf_counter()
#     await asyncio.sleep(delay)
#     print(tag, "done in", f'{time.perf_counter() - t0:.2f}s')
#
#
# async def main():
#     await asyncio.gather(
#         coro('f', 8),
#         coro('c', 4),
#         coro('a', 5),
#         coro('b', 3)
#     )
#
#
#
# asyncio.run(main())
#
#
# import asyncio
# import time
#
# async def fake_request(name, delay):
#     await asyncio.sleep(delay)
#     return f'{name} ok'
#
#
# async def sequential():
#     t0 = time.perf_counter()
#     await fake_request('a', 1)
#     await fake_request('b', 1)
#     print('sequential time:', time.perf_counter() - 10)
#
#
# async def parallel():
#     t0 = time.perf_counter()
#     await asyncio.gather(
#         fake_request('a', 1),
#         fake_request('b', 1)
#     )
#     print("parallel time", time.perf_counter() - 10)
#
#
# asyncio.run(sequential())
# asyncio.run(parallel())


#
# async def hello():
#     print('hello')
#
#
# asyncio.run(hello())
#
#
#
# import asyncio
#
#
# async def long():
#     await asyncio.sleep(2)
#     return 'hello'
#
#
# async def main():
#     task = asyncio.create_task(long())
#     print('doing something')
#     await asyncio.sleep(1)
#     print('result', await task)
#
#
# asyncio.run(main())
#
#


import asyncio
import random

sem = asyncio.Semaphore(2)


async def download(i):
    async with sem:
        await asyncio.sleep(random.uniform(0.5, 1.5))
        print(f'file {i} download')


async def main():
    await asyncio.gather(*(download(i) for i in range(10))


asyncio.run(main())
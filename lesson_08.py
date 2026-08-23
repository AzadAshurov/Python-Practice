import asyncio
import time


async def task(name: str, delay: float):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 5),
        task("C", 1),
        task("D", 3),
        task("E", 4)
    )

start = time.perf_counter()

asyncio.run(main())

print(f"Total: {time.perf_counter() - start:.2f} sec")
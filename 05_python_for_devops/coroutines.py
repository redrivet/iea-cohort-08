import asyncio

# Async declares this as a coroutine
async def blip_on_2():
    # Await yields control to the event loop
    for i in range(10):
        await asyncio.sleep(2)
        print(f"Blip #{i}!")


# Coroutines can take args, just like regular functions
async def bloop_on_X(x):
    for i in range(10):
        await asyncio.sleep(x)
        print(f"Bloop #{i}!")


async def read_poem():
    with open("poem.txt") as poem:
        for line in poem:
            print(line)
            await asyncio.sleep(0.5)


async def main():
    # Create tasks so these coroutines can all run concurrently
    blip_task = asyncio.create_task(blip_on_2())
    bloop_task = asyncio.create_task(bloop_on_X(3))
    read_poem_task = asyncio.create_task(read_poem())

    print("Main: Waiting on tasks to complete!")
    # Wait for all tasks to complete
    await blip_task
    await bloop_task
    await read_poem_task
    print("All Done!")


# Starts the event loop with the main() coroutine
asyncio.run(main())

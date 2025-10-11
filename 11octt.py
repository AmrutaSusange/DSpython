import time
import asyncio

async def llm(semaphore):
    async with semaphore:
        print('making request to openai')
        await asyncio.sleep(1.5)
        print('got the response')

async def main():
    semaphore = asyncio.Semaphore(16)
    tasks = []
    for i in range(10000):
        tasks.append(asyncio.create_task(llm(semaphore)))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())

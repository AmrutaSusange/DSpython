import time
import asyncio

async def take_metro_ticket(i):
    print('started')
    await asyncio.sleep(i)
    print('done')

async def run_code():
    people_in_queue = [1,1,3,4,5,3,4,12]
    s = time.time()
    t = [asyncio.create_task(take_metro_ticket(each)) for each in people_in_queue]
    await asyncio.gather(*t)
    e = time.time()
    print('done in ', e-s)

if __name__ == '__main__':
    asyncio.run(run_code())






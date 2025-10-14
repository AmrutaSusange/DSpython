import asyncio
import time
async def background_task():
    for i in range(10):
        print(f"[Background] Working... {i}")
        time.sleep(1)
    print("[Background] Done.")

async def user_input_task():
    user_input = await asyncio.to_thread(input, 'write something__' )
    print(f"[User Input] You typed: {user_input}")

async def main():
    t = [background_task() for each in range(8)]
    await asyncio.gather(user_input_task(),*t)

if __name__ == "__main__":
    asyncio.run(main())

# what calls next task in async
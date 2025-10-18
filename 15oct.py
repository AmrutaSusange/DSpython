'''Concurrency or Parallelism
Notes

Task-level concurrency
asyncio (coroutines)

✅ Concurrency
Runs multiple tasks in a single thread using event loop

Thread-level concurrency
ThreadPoolExecutor / threading
✅ Concurrency (limited parallelism)
Multiple threads can interleave, useful for I/O-bound tasks


Process-level parallelism
multiprocessing / ProcessPoolExecutor
✅✅ True parallelism
Multiple processes, each with its own GIL and CPU core

✅ asyncio → Task-level concurrency (single thread)
✅ ThreadPoolExecutor → Thread-level concurrency (multi-threaded I/O)
✅ multiprocessing → Process-level parallelism (multi-core true parallel execution)

'''

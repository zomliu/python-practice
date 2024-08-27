import asyncio, time

# asyncio 基本使用
# Video Reference: 
#   - https://www.youtube.com/watch?v=YRocKEfLMTk&list=PLvQDgAXJ4ADMzlySkwIGomEA9j1Vgq5uS&index=22
#   - https://www.youtube.com/watch?v=G5dBku_NDns&list=PLvQDgAXJ4ADMzlySkwIGomEA9j1Vgq5uS&index=23

async def print_num(name : str, sleep : int):
    print(f'{name} start')
    await asyncio.sleep(sleep)
    print(f'{name} end')
    return name

async def task_with_exception():
    print('task with exception start')
    raise Exception('task with exception')

async def entrance():
    time_start = time.perf_counter()
    task_a = asyncio.create_task(print_num('A', 2))
    task_b = asyncio.create_task(print_num('B', 3))

    await task_a
    print('task_a finished')
    await task_b
    print('task_b finished')

    end_start = time.perf_counter()
    print(f'cost time: {end_start - time_start}')


async def entrance_with_cancel():
    task_a = asyncio.create_task(print_num('A', 2))
    task_b = asyncio.create_task(print_num('B', 3))

    await task_a
    if not task_b.done():
        task_b.cancel()
        print('task_b canceled')
    
    print('function finished')
    

async def entrance_with_timeout():
    task_a = asyncio.create_task(print_num('A', 2))
    try:
        await asyncio.wait_for(task_a, timeout=3)
        # await asyncio.wait_for(asyncio.shield(task_a), timeout=3)
        print('task_a finished')
    except asyncio.TimeoutError:
        print('task_a timeout')
    
    # asyncio.shield 可以保护任务，防止任务被取消, 不过可能会导致任务无法正常取消或者阻塞, 需要在 except 中处理任务(取消或者等待)
    # try:
    #     await asyncio.wait_for(asyncio.shield(task_a), timeout=3)
    #     print('task_a finished')
    # except asyncio.TimeoutError:
    #     print('task_a timeout')
    #     # task_a.cancel()
    #     await task_a

async def entrance_with_gather():
    task_a = asyncio.create_task(print_num('A', 2))
    task_b = asyncio.create_task(print_num('B', 3))

    # return_exceptions=True 可以返回异常, 默认为 False, 会把异常抛出
    result = await asyncio.gather(task_a, task_b, asyncio.create_task(task_with_exception()), return_exceptions=True)
    
    print(result)

if __name__ == '__main__':
    # asyncio.run(entrance())
    # asyncio.run(entrance_with_cancel())
    # asyncio.run(entrance_with_timeout())
    asyncio.run(entrance_with_gather())
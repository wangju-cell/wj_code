import asyncio
import time

async def _task():
    print(f"{time.strftime('%H:%M:%S')}task 开始")
    time.sleep(2)
    print(f"{time.strftime('%H:%M:%S')}task 结束")
    return "运行结束"

def callback(task):
    print(f"{time.strftime('%H:%M:%S')}回调函数开始运行")
    print(f"状态：{task.result()}")

if __name__ == '__main__':
    print(f"产生一个协程对象但是不开始执行{_task()}")

    #开始构造task任务才能绑定回调函数
    task =asyncio.ensure_future(_task())
    #给他绑定回调函数
    task.add_done_callback(callback)
    print("开始运行协程，要有loop对象才能开始运行，跟线程，进程不一样，不能直接 start")
    loop=asyncio.get_event_loop()
    loop.run_until_complete(task)
    print("协程和回调函数执行完毕")



#这个协程任务运行完毕之后，可以跑回去看下之前自己是否运行成功了
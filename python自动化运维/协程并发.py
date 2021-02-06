import asyncio
import time

async  def task():
    print(f"{time.strftime('%H:%M:%S')} task 开始")
    await asyncio.sleep(2)
    print(f"{time.strftime('%H:%M:%S')} task 结束")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks=[task() for _ in range(5)] #生成一个列表tasks ，由5个task()组成
    start=time.time()
    loop.run_until_complete(asyncio.wait(tasks))  #让5个任务并发执行，没有先后顺序
    loop.close()
    end=time.time()
    print(f"用时间{end-start}秒")



#这里并没有使用多进程或者多线程，从而实现了并发，task可以替换为任意耗时较高的IO操作函数
#当你只想要循环5次, 而不需要引用计数值, 不想给这个计数值起名字, 那么就把它叫做_吧

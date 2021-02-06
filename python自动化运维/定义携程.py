import asyncio
import time

async def task():
    print(f"{time.strftime('%H:%M:%S')}task 开始")
    time.sleep(2)
    print(f"{time.strftime('%H:%M:%S')}task 结束")

xiecheng=task()

print(f"{time.strftime('%H:%M:%S')}产生协程对象{xiecheng},但是函数并未被调用")
loop=asyncio.get_event_loop() #用该方法创建一个时间循环loop
print(f"{time.strftime('%H:%M:%S')} 开始调用协程任务")
starttime=time.time()
loop.run_until_complete(xiecheng) #将协程注册到事件循环loop中去
end=time.time()
print(f"{time.strftime('%H:%M:%S')}结束协程调用，耗时{end-starttime}")


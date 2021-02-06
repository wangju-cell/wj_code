import asyncio
import time
import aiohttp

#aiohttp 是一个支持异步请求的库，和requests库不同，request是不支持异步请求的

now = lambda : time.strftime("%H:%M:%S")
print(now())

async def get(url):
    session= aiohttp.ClientSession()
    response=await session.get(url)
    result=await response.text()
    session.close()
    return result

async def request():
    url="http://127.0.0.1:5000"
    #这个程序的基础是，"协程的异步请求-简单的web服务" 这个python文件要处于运行中，并提供web服务
    print(f"{now()}请求{url}")
    result=await get(url)
    print(f"{now()}得到响应{result}")

if __name__ == '__main__':
    start=time.time()
    tasks = [asyncio.ensure_future(request()) for _ in range(5)]
    #协程对象是无法执行的，只有生成协程任务，或者协程任务列表，使用loop来执行。
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    #这里的wait方法，意思是等待协程任务全部运行，再把结果收集起来

from multiprocessing.dummy import Pool as ThreadPool
import time

def fun(n):
    time.sleep(2)
start = time.time()
for i in range(5):
    fun(i)
print(f"单线程顺序执行耗时：{time.time()-start}")


start2=time.time()
pool=ThreadPool(processes=5) #线程池最大容纳5个线程，如果不设置值的话，默认能够开启CPU核心数的线程数。
result=pool.map(fun,range(5)) #往线程池里面去放线程任务，之后自动开始执行，不需要start
pool.close() #关闭线程池，不再接受新的进程，只是关闭，资源并未被释放
pool.join() #主线程程阻塞等待子线程的退出
print("线程池5个线程并发执行耗时：",time.time()-start2)

#关于线程池，每一个单独的线程执行完任务后，会被重新回收到线程池中，继续等待下一个需要执行的任务
#然而t.start  t.join是不断的在创建和销毁对象，这种机制更加的耗费系统资源。



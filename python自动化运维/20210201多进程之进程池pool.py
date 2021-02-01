#poll可以提供指定数量的进程供用户调用，当有新的请求提交到pool中的时候
# 如果池还没有满，就会创建一个新的进程供用户调用，
#若果池中的进程数量已经达到了最大值，该请求就会停止，直到池中有进程结束时才会创建新的进程

import multiprocessing
import time

def task(name):
    print(f"{time.strftime('%H:%M:%S')}:{name}开始执行")
    time.sleep(3)

if __name__ == '__main__':
    #维持执行的进程总数为3个，当一个进程执行完毕后会再次添加新的进程进去，跟之前的队列比较像
    pool=multiprocessing.Pool(processes=3)
    for i in range(10):
        pool.apply_async(func=task,args=(i,))
        # pool.apply(func=task, args=(i,))

    pool.close()
    pool.join()
    print("hello")

#apply(): 阻塞主进程, 并且一个一个按顺序地执行子进程, 等到全部子进程都执行完毕后 ,继续执行 apply()后面主进程的代码
# apply_async() 非阻塞异步的, 他不会等待子进程执行完毕, 主进程会继续执行, 他会根据系统调度来进行进程切换
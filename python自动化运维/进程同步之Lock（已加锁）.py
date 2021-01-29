#多进程的目的是并发执行，提高资源利用率，从而提高效率，但是有些时候
#我们需要在某一时间只能有一个进程访问某个共享资源的话，就需要使用锁lock

import multiprocessing
import time

def task1(lock):
    with lock:
        n=5
        while n>1:
            print(f"{time.strftime('%H:%M:%S')} task1 输出信息")
            time.sleep(1)
            n-=1

def task2(lock):
    lock.acquire()
    n=5
    while n>1:
        print(f"{time.strftime('%H:%M:%S')} task2 输出信息")
        time.sleep(1)
        n-=1
    lock.release()

def task3(lock):
    lock.acquire()
    n=5
    while n>1:
        print(f"{time.strftime('%H:%M:%S')} task3 输出信息")
        time.sleep(1)
        n-=1
    lock.release()

if __name__ == '__main__':
    #先初始化一个锁的实例，然后在需要独占的代码前后加锁，with/acquire+relaease均可
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=task1,args=(lock,))
    p2 = multiprocessing.Process(target=task2,args=(lock,))
    p3 = multiprocessing.Process(target=task3,args=(lock,))
    p1.start();p2.start();p3.start()


#可以看到输出结果，同一个时间点，只有1条信息输出出来。
#他和信号量控制并发，区别是信号量可以控制有多少个进程同时运行
#而锁是用来保护某个进程的，但使用信号量的时候最好是给某个进程加上锁。
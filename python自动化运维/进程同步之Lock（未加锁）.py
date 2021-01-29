#多进程的目的是并发执行，提高资源利用率，从而提高效率，但是有些时候
#我们需要在某一时间只能有一个进程访问某个共享资源的话，就需要使用锁lock

import multiprocessing
import time

def task1():
    n=5
    while n>1:
        print(f"{time.strftime('%H:%M:%S')} task1 输出信息")
        time.sleep(1)
        n-=1

def task2():
    n=5
    while n>1:
        print(f"{time.strftime('%H:%M:%S')} task2 输出信息")
        time.sleep(1)
        n-=1

def task3():
    n=5
    while n>1:
        print(f"{time.strftime('%H:%M:%S')} task3 输出信息")
        time.sleep(1)
        n-=1
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)
    p3 = multiprocessing.Process(target=task3)
    p1.start();p2.start();p3.start()


#可以看到输出结果，同一个时间点，有不同的信息输出出来。
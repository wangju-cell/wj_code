from multiprocessing import Process
import os
import time

def task_process(delay):
    num=0
    for i in range(delay*100000000):
       num+=1
    print(f"进程pid为{os.getpid()},执行完成")


if __name__ == '__main__':
    print(f'父进程为pid{os.getpid()}')
    t0=time.time()
    task_process(3)
    task_process(3)
    t1=time.time()
    print(f'顺序执行时间为{t1-t0}')
    p0=Process(target=task_process,args=(3,))
    p1=Process(target=task_process,args=(4,))
    t2=time.time()
    p0.start();p1.start()
    p0.join();p1.join()
    t3=time.time()
    print(f'多进程并发执行的时间是{t3-t2}')

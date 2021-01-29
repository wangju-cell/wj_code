from multiprocessing import Process
import os
import time

#子进程需要执行的代码
def task_process(delay):
    print(f"{time.strftime('%y-%m-%d %H-%M-%S')}子进程开始")
    print(f"sleep {delay}s")
    time.sleep(delay)
    print(f"{time.strftime('%y-%m-%d %H-%M-%S')}子进程结束")

if __name__ == '__main__':
    print(f"{time.strftime('%y-%m-%d %H-%M-%S')}父进程开始")
    p0=Process(target=task_process,args=(3,))
    #设置daemon为True,意思是父进程不需要等待子进程，父进程一结束整个进程直接结束
    #并且该属性是设置在子进程上的
    p0.daemon=True
    p0.start()
    print(f"{time.strftime('%y-%m-%d %H-%M-%S')}父进程结束")
from multiprocessing import Process
import os
import time

class MyProcess(Process):

    def __init__(self,delay):
        self.delay = delay
        super().__init__()

    # 子进程需要执行的代码
    def run(self):
        num=0
        for i in range(self.delay*100000000):
            num+=1
        print(f"进程pid为：{os.getpid()},执行完成")
if __name__ == '__main__':
    print(f"父进程pid为{os.getpid()}")
    p0=MyProcess(3)
    p1=MyProcess(3)
    t0=time.time()
    p0.start()
    p1.start()
    p0.join()
    p1.join()
    t1=time.time()
    print(f"多进程并发执行时间耗时{t1-t0}")

#为什么要用supper
# super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
# MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表

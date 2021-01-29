#semaphore用来控制对共享资源的访问数量，可以控制同一时刻并发的进程数量

import multiprocessing
import time

def worker(s,i):
    s.acquire() #意思是接受传入的进程并发限制策略
    print(time.strftime('%y-%m-%d %H-%M-%S'),multiprocessing.current_process().name+"获得锁运行")
    time.sleep(i)
    print(time.strftime('%y-%m-%d %H-%M-%S'), multiprocessing.current_process().name+"释放锁结束")
    s.release()

if __name__ == '__main__':
    s=multiprocessing.Semaphore(2)
    for i in range(6):
        p=multiprocessing.Process(target=worker,args=(s,2))
        p.start()


#samphore又叫做信号量，是进程加锁的一种方式
# acquire()用来获取锁，release()用来释放锁。当一个进程调用acquire()时，
# 如果锁的状态为unlocked，那么会立即修改为locked并返回，这时该进程即获得了锁。如果锁的状态为locked，那么调用acquire()的进程则阻塞。
import time,threading
num= 0

# 不带锁的写法
# def task_thread(n):
#     global num
#     for i in range(1000000):
#         num =num+n
#         num=num-n

#带锁的写法
lock=threading.Lock()
def task_thread(n):
    global num
    #开启锁，用于线程同步
    lock.acquire()
    for i in range(1000000):
        num=num+n
        num=num-n
    #释放锁用于开启下一个线程
    lock.release()

t1=threading.Thread(target=task_thread,args=(6,))
t2=threading.Thread(target=task_thread,args=(17,))
t3=threading.Thread(target=task_thread,args=(11,))
t1.start();t2.start();t3.start()
t1.join();t2.join();t3.join()

print(num)
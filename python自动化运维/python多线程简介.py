import os,time
from multiprocessing import Process
from threading import Thread

#计算密集型程序-多进程实现  对比多线程实现
def work():
    res=0
    for i in range(200000000):
        res*=i
def ioworkk():
    time.sleep(2)
    print("===>",file=open("tmp.txt","w"))

if __name__ == '__main__':
    l=[]
    print("本机为",os.cpu_count(),"核CPU")
    start = time.time()
    for i in range(4):
        p=Process(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop=time.time()
    print('计算密集型程序-多进程耗时：',stop-start)

    l.clear()
    start2=time.time()
    for i in range(4):
        t=Thread(target=work)
        t.start()
        l.append(t)
    for i in l:
        i.join()
    stop2=time.time()
    l.clear()
    print("计算型密集程序-多线程耗时：",stop2-start2)


    print('开始IO测试>>>>>>>>>>>>>>>>>>>>>>')
    print("本机为", os.cpu_count(), "核CPU")
    start3=time.time()
    for i in range(400):
        p=Process(target=ioworkk)
        l.append(p)
        p.start()
    for p in l:
        p.join()
    stop3=time.time()
    print("io密集型程序-多进程耗时",stop3-start3)

    print("本机为", os.cpu_count(), "核CPU")
    start4 = time.time()
    for i in range(400):
        t = Thread(target=ioworkk)
        l.append(t)
        t.start()
    for t in l:
        t.join()
    stop4 = time.time()
    print("io密集型程序-多线程耗时", stop4 - start4)






#计算密集型程序，




#IO密集型程序，多线程实现


#IO密集型程序，多进程实现
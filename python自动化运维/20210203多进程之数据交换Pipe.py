import multiprocessing
import time

def task1(pipe):
    for i in range(5):
        str=f"'task1-{i}"
        print(f"{time.strftime('%H:%M:%S')}task1 发送：{str}")
        pipe.send(str)
    for i in range(5):
        print(f"{time.strftime('%H:%M:%S')}task1 接受：{pipe.recv()}")

def task2(pipe):
    for i in range(5):
        print(f"{time.strftime('%H:%M:%S')}task2 接受{pipe.recv()}")
    time.sleep(1)
    for i in range(5):
        str = f"'task12-{i}"
        print(f"{time.strftime('%H:%M:%S')}task2 发送：{str}")
        pipe.send(str)


if __name__ == '__main__':
    pipe=multiprocessing.Pipe()
    p1=multiprocessing.Process(target=task1,args=(pipe[0],))
    p2=multiprocessing.Process(target=task2,args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

#为什么能够使用pipe[0], pipe[1]这种写法，是因为Pipe天生就具备两个端口，一个负责收，一个负责发送，并且是全双工的。
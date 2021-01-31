#event用来实现进程之间的通信

import multiprocessing
import time

def wait_for_events(e):
    e.wait()
    time.sleep(1)
    #唤醒后清除event状态，为后续继续等待做准备
    e.clear()
    print(f"{time.strftime('%H:%M:%S')}进程A：我们是兄弟，我等你。。。")
    e.wait()
    print(f"{time.strftime('%H:%M:%S')}进程A：好的，是兄弟一起走")

def  wait_for_event_timeout(e,t):
    e.wait()
    time.sleep(1)
    #唤醒后清除event状态，为后续继续等待做准备
    e.clear()
    print(f"{time.strftime('%H:%M:%S')}J进程B：好吧最多等你{t}秒")
    e.wait(t)
    print(f"{time.strftime('%H:%M:%S')}进程B：我继续往前走了")

if __name__ == '__main__':
    e=multiprocessing.Event()
    w1=multiprocessing.Process(target=wait_for_events,args=(e,))
    w2=multiprocessing.Process(target=wait_for_event_timeout,args=(e,5))
    w1.start();w2.start()
    print(f"{time.strftime('%H:%M:%S')}主进程：谁等我下，我需要8秒时间")
    #唤醒处于等待中的w1,和w2
    e.set()
    time.sleep(8)
    print(f"{time.strftime('%H:%M:%S')}主进程：好了，我赶上了")
    e.set()
    w1.join()
    w2.join()
    print(f"{time.strftime('%H:%M:%S')}主进程：退出。")
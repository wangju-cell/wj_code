import threading,time
import queue

#先进先出
# q=queue.Queue(maxsize=5)
#后进先出
# q=queue.LifoQueue(maxsize=3)
#优先级队列
q=queue.PriorityQueue(maxsize=3)

def produce():
    count=1
    while True:
        q.put(f"冷饮{count}")
        print(f"{time.strftime('%H:%M:%S')}A 放入：[冷饮{count}]")
        count+=1
        time.sleep(1)

def consumer():
    while True:
        print(f"{time.strftime('%H:%M:%S')}B 取出：[{q.get()}]")
        time.sleep(5)


#之所以一个睡5秒，一个睡觉1秒，目的是，生产得快，但是消费的慢，在不用队列阻塞的情况的下，肯定是会爆仓的
#但是使用了队列，就可以使生产者和消费者的速度保持在一个平衡上，maxsize就是一个很好的体现。

if __name__ == '__main__':
    p=threading.Thread(target=produce)
    c=threading.Thread(target=consumer)
    c.start()
    p.start()

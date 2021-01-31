#使用多进程实现生产者-消费者模式
from multiprocessing import Process,Queue
import time
def produceerA(q):
    count=1
    while True:
        q.put(f"冷饮{count}")
        print(f"{time.strftime('%H:%M:%S')}A 放入：【冷饮{count}】")
        print(f"当前有{q.qsize()}个饮料在冰箱")
        count+=1
        time.sleep(1)

def consumenrB(q):
    while True:
        print(f"{time.strftime('%H:%M:%S')}B取出：【{q.get()}】")
        print(f"当前有{q.qsize()}个饮料在冰箱")
        time.sleep(5)
if __name__ == '__main__':
    q=Queue(maxsize=5)
    p=Process(target=produceerA,args=(q,))
    c=Process(target=consumenrB,args=(q,))
    c.start()
    p.start()
    c.join()
    p.join()

#设置了队列最大的容量是5，生产者不停的生产冷饮，消费就不停的取出冷饮，当队列满的时候
# 生产者等待，当队列空的时候，消费者等待，他们取出和放入的速度可能不一致，但是使用队列，就可以让生产者和消费者有条不紊的一直进行下去。
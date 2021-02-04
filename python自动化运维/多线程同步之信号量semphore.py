import threading
import time

#同一时间只有5个人办理业务
semphore = threading.BoundedSemaphore(5)
#模拟银行业务办理
def yewubanli(name):
    semphore.acquire()
    time.sleep(3)  #之所以sleep， 是因为睡一会之后，才能够制造出，5个线程都到位阻塞的情况
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}-{name}在办理业务")
    semphore.release()

thread_list=[]
for i in range(12):
    t=threading.Thread(target=yewubanli,args=(i,))
    thread_list.append(t)

for i in thread_list:
    i.start()



for i in thread_list:
    i.join()


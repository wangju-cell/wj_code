from watchdog.observers import Observer
import time
from watchdog.events import *

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    #检测文件移动的方法
    def on_moved(self, event):
        now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{now} 文件由{event.src_path}移动至{event.dest_path}")
        else:
            print(f"{now}文件由{event.src_path}移动至{event.dest_path}")

    #检测文件是否被创建
    def on_created(self, event):
        now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{now} 文件夹{event.src_path}创建")
        else:
            print(f"{now}文件{event.src_path}创建")

    #检测文件是否被删除
    def on_deleted(self, event):
        now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{now}文件夹{event.src_path}被删除")
        else:
            print(f"{now}文件{event.src_path}被删除")

    #检测文件是否被修改
    def on_modified(self, event):
        now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{now}文件夹{event.src_path}被修改")
        else:
            print(f"{now}文件{event.src_path}被修改")
if __name__ == '__main__':
    observer=Observer()
    path=r"C:\Users\Administrator\Desktop\python\测试watchdog"
    event_handler=FileEventHandler()
    #对path下的目录进行递归
    observer.schedule(event_handler,path,True)
    print(f"监控目录：{path}")
    observer.start()
    observer.join()  #阻塞进程，让其一直处于监控状态

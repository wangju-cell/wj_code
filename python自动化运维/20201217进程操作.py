import os
import psutil
import signal
import time

def show_all():
    for p in psutil.process_iter(attrs=['name','pid','exe','cmdline']):
        print(p.info)


#按照进程名字查看相关信息
def find_procs_by_nmae(name):
    ls=[]
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name']==name:
            ls.append(p)
    return ls


#按照名称查看相关信息2
def find_procs_by_name2(name):
    ls=[]
    for p in psutil.process_iter(attrs=["name","exe","cmdline"]):
        if name == p.info['name'] or \
                p.info('exe') and os.path.basename(p.info['exe'])==name or \
                p.info['cmdline'] and p.info['cmdline'][0]==name:
            ls.append(p)
    return ls

#杀掉进程树
def kill_procs_tree(pid,sig=signal.SIGTERM,include_parent=True,timeout=None,on_terminate=None):
    '''杀掉进程树，包括子进程，'''
    #如果用户填入的pid刚好是程序执行的进程号，直接报错，不再执行下一步
    if pid==os.getpid():
        raise RuntimeError("i refuse kill myself")
    parent=psutil.Process(pid)
    children=parent.children(recursive=True)
    print("原始parent:", parent)
    print("原始children:",children)

    if include_parent:
        children.append(parent)
        print("添加后的chiLdren",children)
    exit()
    for p in children:
        p.send_signal(sig)

    gone,alive =psutil.wait_procs(children,timeout=timeout,callback=on_terminate)

    return (gone,alive)


if __name__ == '__main__':
    #find_procs_by_name2("WeChat")
    show_all()
    kill_procs_tree(4256)



# 等待一组process实例终止，返回一个(gone, alive)元组，指示哪些进程已经消失，那些进程仍在运行。消失的进程将具有一个新的returncode属性，
# 该属性指示Process.wait（）函数返回的进程退出状态。 callback是一个函数，当一个正在等待的进程终止时，将调用该函数，
# 并将Process实例作为回调参数传递（该实例还将设置一个returncode属性）。 所有进程终止或发生超时（秒）后，此函数将返回。
# 与Process.wait（）不同，如果发生超时，它将不会引发TimeoutExpired。

# SIGTERM等信号含义
# ① SIGINT     终止进程     中断进程
#
# 程序终止(interrupt)信号, 在用户键入INTR字符(通常是Ctrl-C)时发出。
#
# ② SIGQUIT    建立CORE文件终止进程，并且生成core文件
#
# ③ SIGQUIT 和 SIGINT 类似，但由QUIT字符(通常是Ctrl-)来控制；进程在因收到SIGQUIT退出时会产生core文件，在这个意义上类似于一个程序错误信号。
#
# ④ SIGKILL    终止进程     杀死进程
#
# ⑤ SIGPIPE    终止进程     向一个没有读进程的管道写数据
#
# ⑥ SIGALARM    终止进程     计时器到时
#
# ⑦ SIGTERM    终止进程     软件终止信号
#
# ⑧ SIGTERM 程序结束(terminate)信号，与SIGKILL不同的是该信号可以被阻塞和处理。
# 通常用来要求程序自己正常退出。shell命令kill缺省产生这个信号。SIGTERM is the default signal sent to a process by the kill or killall commands.
#
# ⑨ SIGURG    忽略信号     I/O紧急信号
#
# ⑩ SIGIO    忽略信号     描述符上可以进行I/O
#
# 11 SIGCHLD    忽略信号     当子进程停止或退出时通知父进程
#
# 有两个信号可以停止进程：SIGTERM和SIGKILL。SIGTERM比较友好，进程能捕捉这个信号( it can be caught and interpreted (or ignored) by the process)，
# 根据您的需要来关闭程序。在关闭程序之前，您可以结束打开的记录文件和完成正在做的任务。在某些情况下，假如进程正在进行作业而且不能中断，那么进程可以忽略这个SIGTERM信号。
#
# 对于SIGKILL信号，进程是不能忽略的( this signal cannot be caught or ignored,)。这是一个“我不管您在做什么,立刻停止”的信号。
# 假如您发送SIGKILL信号给进程，Linux就将进程停止在那里。
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging


logger=logging.getLogger()   #记录日志，默认情况下仅输出到终端（屏幕），这里既输出到终端又输出到文件，方便日志查看
logger.setLevel(logging.INFO)
ch=logging.StreamHandler()
fh=logging.FileHandler(filename='myftpserver.log',encoding='utf-8')
#默认的方式是追加到文件

ch.setFormatter(LogFormatter())
fh.setFormatter(LogFormatter())

logger.addHandler(ch) #将日志输出到屏幕
logger.addHandler(fh) #将日志输出到文件

#实例化虚拟用户，这是FTP验证的首要条件
authorizer=DummyAuthorizer()
#添加用户权限和路径，并设置用户名，密码，用户目录，权限，可以为不同的用户添加不同的权限
authorizer.add_user("user","12345","d:/",perm="elradfmw")

#t添加匿名用户，只需要路径
authorizer.add_anonymous("d:/")

#初始化ftp句柄
handler=FTPHandler
handler.authorizer=authorizer

#添加被动端口范围
handler.passive_ports=range(2000,2333)

#设置上传下载的速度
dtp_handler=ThrottledDTPHandler
dtp_handler.read_limit=300*1024   #300kb/s
dtp_handler.write_limit=300*1024  #300kb/s
handler.dtp_handler=dtp_handler

#监听ip和端口，linux里需要root用户才能使用21端口
server=FTPServer(("0.0.0.0",21),handler)

#设置最大连接数
server.max_cons=150
server.max_cons_per_ip=15

#开始ftp服务，并打印出日志信息
server.serve_forever()


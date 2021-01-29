#设置日志的级别
import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     filename='./lx_log1.log',
#     filemode='w'
# )
#
# #设置完日志模块后，开始使用日志输出模块
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warn message')
# logging.error('error message')
# logging.critical('critical message')
# print('对的')

#如果本段代码输出日志到文件中,中文显示乱码的话，那是因为，没有对logging.Filehandler设置utf8编码
#下面的代码的将会按照loggign模块的规范进行操作
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#将日志信息打印在终端的同时，也写入日志文件
#创建记录器，并设置及录器的名字，设置记录日志的级别
logger=logging.getLogger('simple_example')
print(logger.name)
logger.setLevel(logging.INFO)

#创建两个handler，1个负责输出到终端，1个负责输出到文件，并分别设置他们的日志级别
ch=logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh=logging.FileHandler(
    filename='simple.log',mode='a',encoding="utf-8"
)
fh.setLevel(logging.WARNING)

#创建1个格式化器，可以创建出不同的格式用于不同的handler,
formatter=logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(message)s"
)

#设置上面创建的两个handler的格式化
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#为创建的logger添加handler
logger.addHandler(ch)
logger.addHandler(fh)

#开始记录日志
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")



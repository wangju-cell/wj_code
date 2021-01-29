import logging
import logging.config

#logging的配置信息已经写好在logging.config文件里面了
logging.config.fileConfig('logging.config')

#创建1个logger
logger=logging.getLogger('simpleexample')

#开始记录日志
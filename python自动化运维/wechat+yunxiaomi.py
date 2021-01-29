#encoding =utf-8
from wxpy import *
from requests import *
import base64
import urllib.parse
import hmac
from hashlib import sha1
import requests
import uuid
import time
from time import sleep
from aliyun_chat import *

import hmac, ssl
#开启缓存功能，使其短时间内不用扫码
bot=Bot(cache_path=True)

#机器人自身账号
myself = bot.self

# #启用puid属性，并指定puid所需的映射数据保存/载入路径，puid可始终被获取到，具有稳定的唯一性
bot.enable_puid("wxpy_puid.pkl")

# #通过名称查找1个好友，并显示他的uid
my_friend = bot.friends().search("老婆")[0]
my_mom = bot.friends().search("李平兰")[0]
print(my_friend.puid)
my_friend.send("过来耍")
my_mom.send("妈妈在干啥")

#给家庭群发消息
groups=bot.groups()
my_group = groups.search("相亲相爱一家人")[0]
# my_group.send("晚上好，小小机器人向你们问好")


# 回复 my_friend 发送的消息
@bot.register(Friend)
def reply_my_friend(msg):
    print(msg.text)
    res = msg.text
    response = robot(res)
    print(response)
    msg.reply(response)

# 回复发送给自己的消息，可以使用这个方法来进行测试机器人而不影响到他人
@bot.register(bot.self, except_self=False)
def reply_self(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)

# 打印出所有群聊中@自己的文本消息，并自动回复相同内容
# 这条注册消息是我们构建群聊机器人的基础
@bot.register(Group, TEXT)
def print_group_msg(msg):
    if msg.is_at:
        print(msg)
        res=robot(msg.text)
        print(res)
        sleep(1)
        msg.reply(res)



embed()

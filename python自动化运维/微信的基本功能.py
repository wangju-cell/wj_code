#encoding =utf-8
from wxpy import *
#开启缓存功能，使其短时间内不用扫码
bot=Bot(cache_path=True)

#机器人自身账号
myself = bot.self

# #微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

#发送消息给自己
# bot.self.send("能收到吗？")

#向文件传输助手发送消息
bot.file_helper.send("你好，文件助手")
#
# #启用puid属性，并指定puid所需的映射数据保存/载入路径，puid可始终被获取到，具有稳定的唯一性
bot.enable_puid("wxpy_puid.pkl")

# #通过名称查找1个好友，并显示他的uid
my_friend = bot.friends().search("老婆")[0]
print(my_friend.puid)
my_friend.send("过来耍")

#给家庭群发消息
groups=bot.groups()
my_group = groups.search("相亲相爱一家人")[0]
# my_group.send("晚上好，小小机器人向你们问好")

#这里是接受所有人的消息
@bot.register()
def save_msg(msg):
    print(msg)

#接受特定好友消息，并让图灵机器人自动回复好友消息
@bot.register(Friend)
def save_msg(msg):
    print(msg)
    Tuling().do_reply(msg)  #调用图灵机器人，也可以用自己的api


@bot.register(my_group)
def group_send(msg):
    groups = bot.groups()
    print(f"我收到了消息{msg}")
    Tuling(api_key="40d56dcf5e1d4edc8a891eb824a11437").do_reply(msg)


embed()

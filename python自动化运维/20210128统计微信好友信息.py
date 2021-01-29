from wxpy import *
bot = Bot(cache_path=True)
friends_stat=bot.friends().stats()
friends_loc=[]
for province ,count in friends_stat["city"].items():
    if province !="":
        friends_loc.append([province,count])

#对每个省份的人数降序排列
friends_loc.sort(key=lambda x:x[1],reverse=True)

#打印前10
for item in friends_loc[:]:
    print(item[0],item[1])



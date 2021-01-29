#encoding=utf-8
import configparser
# #实例化configparser类
config=configparser.ConfigParser()
# #读取配置文件
# config.read(r"C:\Users\Administrator\Desktop\python\pip.ini")
# for section in config.sections():
#     print(f"section is [{section}]")
#     for key in config[section]:
#         print(f"key is [{key}],value is [{config[section][key]}]")
#
# print("-----通过键获取相对的值：----------------")
# print(f"index-url is [{config['global']['index-url']}]")
# print(f"trusted-host is [{config['global']['trusted-host']}]")

#>>>>>把内容写入配置文件>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# config["DEFAULT"]={
#     "ServerAliveUInterval":"45",
#     "Compression":"yes",
#     "CompressionLevel":"9",
# }
# config["bitbucket.org"]={}
# config["bitbucket.org"]["user"]="hg"
# config["topscret.server.com"]={}
# topsecret=config["topscret.server.com"]
# topsecret["port"]="50022"
# topsecret["ForwardX11"]="no"
# config["DEFAULT"]["ForwardX11"]="yes"
# with open("example.ini","w") as configfile:
#     config.write(configfile)
#
# with open("example.ini","r") as f:
#     print(type(config["DEFAULT"]["forwardX11"]))
#     print(config["bitbucket.org"]["ServerAliveUInterval"])


#>>>>>python解析xml>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import xml.sax
from xml.dom.minidom import parse
import xml.dom.minidom

#使用minidom解析器打开xmL文档
domtree=xml.dom.minidom.parse("example.xml")
collection=domtree.documentElement
if collection.hasAttribute("year"):
    print(f"这是一个早餐的菜单\n年份{collection.getAttribute('year')}")

foods=collection.getElementsByTagName("food")
for food in foods:
    type=food.getElementsByTagName("name")[0]
    print("name: %s" %type.childNodes[0].data)

    format=food.getElementsByTagName("prices")[0]
    print("price : %s" %format.childNodes[0].data)

    descri=food.getElementsByTagName("description")[0]
    descri=descri.childNodes[0].data.strip()
    print("desctption : %s" %descri)

    cal=food.getElementsByTagName("calories")[0]
    print("calories : %s:" %cal.childNodes[0].data)

    print('\n')




#python内置了poplib模块实现了POP3协议
#第一步，用poplib模块吧邮件的内容的原始文本下载到本地
#第二步，用email模块解析原始文本，还原为邮件对象

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#输入邮件地址，密码，和pop3服务器地址
email = "15718017455@163.com"
password = "GBSSKZCFEPFZFPDI"
pop3_server = "smtp.163.com"

#连接到pop3服务器，如果开启ssl, 就使用poplib.POP_SSL
server = poplib.POP3_SSL(pop3_server)

#可以打开或者关闭调试信息
server.set_debuglevel(1)
#可选，打印POP3服务器的欢迎文字
print(server.getwelcome().decode("utf-8"))

#身份证认证
sever.user(email)
server.pass_(password)

#start返回邮件的数量和占用空间
count = server.stat()[0]
percent = server.stat()[1]/1024/1024
print(f"邮件数量{count}邮件大小为：{percent}")

#list()列出所有邮件编号
resp,mails,octets = server.list()

#获取最新的一封邮件注意索引号从1开始，因此最新邮件的索引即为邮件的总个数
index = len(email)
resp,lines,octets = server.retr(index)

#lines存储了邮件的原始文本的每一行,可以获得整个邮件的原始文本
msg_content = b"\r\n".join(lines).decode("utf-8")
#解析出邮件
msg = Parser().parse(msg_content)

def decode_str(s):
    value,charset=decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

print("解析获取到的邮件内容如下：\n------------------------begin------------------------------")
#打印发件人信息
print(
    f"{decode_str(parseaddr(msg.get('From',''))[0])}<{decode_str(parseaddr(msg.get('From',''))[1])}>"
)
#打印收件人信息
print(
    f"{decode_str((parseaddr(msg.get('To',''))[0]))}<{decode_str(parseaddr(msg.get('To',''))[1])}>"
)
#打印主题信息
print(decode_str(msg["Subject"]))

#打印第一条正文信息
part0 = msg.get_payload()[0]
content = part0.get_payload()(decode=True)
print(content.decode(part0.get_content_charset()))
print('---------------------end------------------------')

#可以根据邮件索引直接从邮件服务器删除邮件
#server.dele(index)
server.quit()


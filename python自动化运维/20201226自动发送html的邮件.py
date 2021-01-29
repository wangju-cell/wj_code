
import smtplib
from email.mime.text import MIMEText

mail_host="smtp.163.com"  #设置smtp服务器域名，一般是邮箱运营商所在的域名
mail_user="15718017455@163.com"
mail_pass="GBSSKZCFEPFZFPDI"

sender="wangju<15718017455@163.com>"
receiver=["wangju<877467349@qq.com>","wangju<wangju193@dingtalk.com>","wangju<15718017455@163.com>"]
#这里的发件人和收件人都需要加<>和前缀， 后者会被当成垃圾邮件回退

message=MIMEText('<html lang="en"><body><h1>这是正文标题</h1>\
<p>正文内容 <a href="www.baidu.com">超链接</a></p>\
</body></html>',"html","utf-8") #构造html的邮件正文


message['From']=sender
message["To"]=";".join(receiver) #构造收件人列表，不是必须的
message["Subject"]="这是邮件主题：SMTP邮件测试"


try:
    smtpobj=smtplib.SMTP()
    smtpobj.connect(mail_host,25)   #25端口为SMTP端口，先要连接服务器，
    smtpobj.login(mail_user,mail_pass) # 然后再登录服务器
    smtpobj.sendmail(sender,receiver,message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败,错误原因:{e}")














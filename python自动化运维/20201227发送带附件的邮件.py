import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

#创建smtp服务
mail_host="smtp.163.com"
mail_user="15718017455@163.com"
mail_passwd="GBSSKZCFEPFZFPDI"

sender="wangju<15718017455@163.com>"
receiver=["wangju<877467349@qq.com>","wangju<wangju193@dingtalk.com>","wangju<15718017455@163.com>"]
message=MIMEMultipart()

message["From"]=sender
message["To"]=";".join(receiver)
message["Subject"]="这是主题：SMTP邮件测试"
message.attach(MIMEText('<p>这是正文：图片及附件发送测试</p><p>图片演示：</p><p><img src="cid:image1"></p>','html','utf-8'))


#指定图片为当前目录
fp=open('1.jpg','rb')
msgimage=MIMEImage(fp.read())
fp.close()

#定义图片id，使其在html中是可用的，
msgimage.add_header("Content-ID","<image1>")
message.attach(msgimage)


#把当前目录下的a.txt作为附件1进行上传
att1=MIMEText(open("a.txt","rb").read(),"base64","utf-8")
att1["Content-Type"]="appliction/octet-stream"
#这里的filename 可以随便写，写什么邮件上就显示什么‘
att1["Content-Disposition"]='attachment;filename="test.txt"'
message.attach(att1)

#添加附件2，传送当前目录下的所有.txt文件
att2=MIMEText(open("测试.txt","rb").read(),"base64","utf-8")
att2["Content-Type"]="application/octet-stream"
#这里的filename 可以随便写，写什么邮件上就显示什么‘
att2.add_header("Content-Disposition","attachment",filename=("gbk","","测试.txt"))
message.attach(att2)

try:
    smtpobj=smtplib.SMTP()
    smtpobj.connect(mail_host,25)
    smtpobj.login(mail_user,mail_passwd)
    smtpobj.sendmail(sender,receiver,message.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print(f"发送失败，原因为：{e}")



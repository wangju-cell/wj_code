from ftplib import FTP

#登录FTP
ftp=FTP(host='localhost',user='user',passwd='12345')

#设置编码方式，由于是在windows系统下运行的，所以选用gbk
ftp.encoding='gbk'
#切换目录
ftp.cwd('test')
#列出文件夹的内容
ftp.retrlines('LIST')  #对应服务端的命令ftp.dir()
#下载文件note.txt
ftp.retrbinary('RETR 123.txt',open('./我是FTP客户端下载的文件.txt','wb').write)
#上传文件ftpserver.py
ftp.storbinary('STOR ftpserver.py',open('20201222FTP服务搭建.py','rb'))
#查看目录下的文件详情
for f in ftp.mlsd(path='/test'):
    print(f)
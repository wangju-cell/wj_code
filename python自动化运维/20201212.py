# -*- coding:utf-8 -*-
f=open("a.txt","w",encoding="utf-8")
f.write("测试w写入,如果文件存在则清理内容后写入；如果文件不存在，则创建\n")
f.close()

f=open("a.txt","a",encoding="utf-8")
f.write("测试a写入方式，如果文件存在，则在文件内容后追加写入；如果不存在，则创建")
f.close()

f=open("a.txt","r",encoding="utf-8")
data=f.read()
print(type(data))
print(data)
f.close()

f=open("a.txt","rb")
data=f.read()
print(type(data))
print(data)

print("将读取的字符进行解码")
print(data.decode('utf-8'))
f.close()

with open('a.txt','w') as f:
    f.write("hello world")

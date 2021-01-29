# -*- coding: utf-8 -*-
# f=open("a.txt","rb+")
# f.write(b"abcdefghi")
# f.seek(5)
# print(f.read(1))
#
# f.seek(-3,2)
# print(f.read(1))
import time
import os
import csv
#基于seeK实现linux命令tail-f的功能
# with open("a.txt",'rb') as f:
#     f.seek(0,2)
#     while True:
#         line=f.read()
#         if line:
#             print(line.decode(('utf-8')),end='')
#         else:
#             time.sleep(0.2)

#小文件的字符串替换
# with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
#     data=read_f.read()
#     print(type(data))
#     data=data.replace('wangju','lianglufan')
#     write_f.write(data)
#
# os.remove('a.txt')
# os.rename('.a.txt.swap','a.txt')

#大文件的字符串替换
import csv
# with open('supper.txt', 'r') as f,open('.a.txt.swap','w') as write_f:
#      for row in f:
#         print(row)
#         row=row.replace('wangju','lianglufan')
#         write_f.write(row)
#
# os.remove('supper.txt')
# os.rename('.a.txt.swap','supper.txt')

#序列化和反序列化
import pickle
data0="hello world"
data1=list(range(20))[1::2]
data2=("x","y","z")
data3={"a":data0,"b":data1,"c":data2}

print(data0)
print(data1)
print(data2)
print(data3)

#>>>>>>开始序列化
output=open("data.pkl","wb")
pickle.dump(data0,output)
pickle.dump(data1,output)
pickle.dump(data2,output)
pickle.dump(data3,output)
output.close()
#>>>>>>>开始反序列化
print("+++++++++++++++++++++++++++")
pkl=open('data.pkl',"rb")
data0=pickle.load(pkl)
data0=pickle.load(pkl)
data0=pickle.load(pkl)
print(data0)


import time
count=0
while True:
    with open("a.txt","a") as f:
        str1="hello world"
        str2=str(time.time())
        strs=str1+str2
        f.write(strs)
        f.write('\n')
        f.flush()
        count+=1
        if count==1000:
            break

# -*- coding:utf-8 -*-
# import chardet
# f = open('tt.txt','r')
# f1=open('file.txt','r')
# data = f.read()
# print chardet.detect(data)
# print chardet.detect(f1.read())
from subprocess import Popen, PIPE
#popen=subprocess.Popen
#pipe=subprocess.PIPE
log=open("os.log","a+")
string=""
p=Popen("ip addr",shell=True,stdout=PIPE)
out=p.stdout.readlines()
for ls in out:
    # print(str(ls, encoding = "utf-8"))
    string=string +str(ls, encoding = "utf-8")
#string=str(out)
log.write(string)
log.close()
#print out
#上面的代码是有问题的估计今天是搞不定了
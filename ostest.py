#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

#测试python在运维管理中的用处

#date 20160815

# author zhu
# os.listdir("路径")列出所有文件和目录
# os.path.isdir（“文件名”）判断是目录吗，是返回True,不是返回False
# os.path.isfile同上判断文件
convertdir=input('please input ')
os.chdir(convertdir)
currentdir=os.getcwd()
print(currentdir)
ls='ls'
dirfiles=[]
files=[]
dirfile =os.popen(ls)
raw_listfile=list(tuple(dirfile))
#print raw_listfile

length=len(raw_listfile)
lst=[]
#print(raw_listfile[0].strip())  #经过实验表明使用strip是一个很好的方法
for i in range(length):
	listfile=raw_listfile[i].strip()#+listfile
	lst.append(listfile)
for x in lst:
	if os.path.isfile(x):
		dirfiles.append(x)
	else:
		files.append(x)
print(dirfiles)
print('------------------')
print(files)
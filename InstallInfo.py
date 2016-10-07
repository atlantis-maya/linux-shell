#!/bin/bash/env python
##############
#关于包安装的模块
#本模块我的想法是可以帮助用户进行包的安装,卸载
#和查询包的安装信息
#
#
##############
class install(object):
	"""在这个类中判断一个package有没有安装"""
	cmdstring="rpm -q"	# 最基本的命令字符串,可以在这个命令上进行扩展
	def __init__(self):
		pass

	def get_softinfo(self,cmdstring):
		"""获得一个package的安装信息"""
		self.info=subprocess.Popen(cmdstring,shell=True,stdout=subprocess.PIPE)
		return self.info

	def get_cmd(self,argument):
		"""得到参数命令,拼接成一个完成的查询安装包的命令"""
		self.cmdstring=self.cmdstring+" "+argument
		return self.cmdstring

	def conver_coding(self,info):
		"""将字节流转换为字符流"""
		self.stringinfo=info.stdout.read().decode("utf-8")
		return self.stringinfo

	# def if_install(self,string):
		"""通过的到的返回值判断这个包有没有被安装"""


#下面是用来测试的代码
if __name__ == '__main__':
	import subprocess
	import re
	i=install()
	info=i.get_softinfo(i.get_cmd('python3'))
	print(i.conver_coding(info))

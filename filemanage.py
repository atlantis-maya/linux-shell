import os
import subprocess

class Filemanage(object):
	#Path=os.path
	"""更改文件的权限"""
	def changeauthority(self,file,path):
		self.file=file
		self.path=path
		if os.path.exists(self.path):
			if os.path.isfile(self.path+"/"+self.file):
				pathfile=self.path+"/"+self.file
				os.system("chmod +x" +" " +pathfile)
				print("执行成功")
			else:
				print("file not find")
		else:
			print("the directory not find")

	def 
if __name__ == '__main__':
	File =Filemanage()
	os.system("pwd")
	os.system("cd /")
	os.system("pwd")
	pwd=input("please input the directory: ")
	file=input("please input  the file: ")
	File.changeauthority(file,pwd)
	"""今天做的主要内容是判断文件是否存在并且判断文件的属性是否"""
#!/bin/bash/env python

import platform
import subprocess


class Platforminfo(object):
	"""docstring for Platforminfo,获取系统信息"""
	def __init__(self, arg):
		super(Platforminfo, self).__init__()
		self.arg = arg
	def get_system(self):
		"""获取计算机系统类型"""
		return platform.system()
	def get_processor(self):
		'''计算机处理器信息'''
		return platform.processor()
	def get_version(self):
		"""获取系统版本号"""
		return platform.version()
	def get_architecture(self):
		"""获取操作系统位数"""
		return platform.architecture
	def get_machine(self):
		"""获取计算机类型"""
		return platform.machine()
	def get_node(self):
		"""计算机的网络名称hongjie-PC"""
		return platform.node()
	def get_uname():
		"""返回值是一个类类型的包含上面所有的返回值"""
		platform.uname()


class NetInfo(object):
	"""docstring for 获取计算机的网络信息 """
	def __init__(self, arg):
		super(NetInfo, self).__init__()
		self.arg = arg
	def get_innerip(self):
		"""得到内网的IP地址"""
		pass
	def get_ip(self):
		"""得到外网的IP地址"""
		pass
	def get_dns(self):
		"""得到dns"""
		pass
	def get_port(self):
		"""得到开放的端口号"""
		pass
	def get_(self):
		pass
class RunInfo(object):
	"""获取运行时的内存和cpu硬盘网络流量的各种信息"""
	def get_free(self):
		"""获取内存的使用情况"""
		pass
if __name__ == '__main__':

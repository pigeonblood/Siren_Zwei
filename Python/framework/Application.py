#-*-coding:utf-8;-*-
from abc import ABCMeta, abstractmethod
from atexit import register
import threading

MaxFPS = 60 

class BaseApplication(metaclass = ABCMeta):
	def __init__(self):
		register(self.AppExit)
		self.AppInit()
		main = threading.Timer(1 / MaxFPS, self.AppUpdate)
		main.start()
	@abstractmethod
	def AppInit(self):
		pass
	@abstractmethod
	def AppUpdate(self):
		pass
	@abstractmethod
	def AppExit(self):
		pass

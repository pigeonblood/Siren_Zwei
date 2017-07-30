#-*-coding:utf-8;-*-

import os
import sys
import os.path as pth

PROJECT_ROOT = pth.abspath(pth.dirname(__file__) + "/..")
MODULE_PATH_CFG = PROJECT_ROOT + "/external.pth"
MODULES = dict()

class ConfigParseError(BaseException):
	pass

def __ModuleInit():
	if not pth.exists(MODULE_PATH_CFG):
		return
	cfg = open(MODULE_PATH_CFG, 'r').read().replace('\r\n','\n').replace(' ', '').replace('\t', '').split('\n')
	ret = []
	for l in cfg:
		if l[0] == '#' or l[:2] == '//':
			continue
		tokens = l.split(' ')
		if tokens[0] == "include" and pth.exists(tokens[1]):
			sys.path.append(tokens[1])
			ret.append(pth.abspath(tokens[1]))
			continue
		if tokens[0] == "exclude" and tokens[1] in sys.path:
			sys.path.remove(tokens[1])
			continue
		raise ConfigParseError("Unexpected token has been found.")
	return 

def LoadModules():
	mdir = __ModuleInit()
	import glob
	for m in mdir:
		for m in glob.glob(m + "/*.py"):
			mn = pth.basename(m).split('.')
			MODULES[mn] = __import__(mn)
	return MODULES


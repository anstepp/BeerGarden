#I think it's really dumb I need both of these here.  But, I get errors when I don't so I leave them.
from multiprocessing import *
import multiprocessing
import subprocess
import sys

count = 0

def homePlayer(*args):
	global count
	for arg in args:
		homeRun = 'PYCMIX < ' + arg
		y = ['/bin/bash', '-c', homeRun]
		subprocess.Popen(y)
	return

def schoolPlayer(*args):
	global count
	for arg in args:
		strikeOut = '/usr/local/src/rtcmix/bin/pycmix < ' + arg
		y = ['/bin/bash', '-c', strikeOut]
		subprocess.Popen(y)
	return
		
def filePlayer(home, commandList):
	if home is True:
		print 'Using home player', '\n'
		p = multiprocessing.Process(target=homePlayer, args=commandList)
		p.start()
		p.join()
	else:
		print 'Using school player', '\n'
		p = multiprocessing.Process(target=schoolPlayer, args=commandList)
		p.start()
		p.join()
	return
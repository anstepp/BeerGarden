#player number one

from rtcmix import *
import random
import math
from probabilityPlay import probabilityPlay  # probabilityPlay(start, directProb, transProb, searchTuple)
from glassReader import fileReturn

#comment/uncomment for send to stereo
#set_option("device = Soundflower (16ch)")

# set params call - change other module(s) if error
rtsetparams(44100, 8, 16)

# to write to file
#set_option("play = off", "clobber = on")
#rtoutput("/Users/anstepp/Desktop/glassesOne.aif")

# load EVERYTHING - prevents some error
load("TRANS")
load("SPECTACLE2")
load("GRANULATE")
load("FREEVERB")

x = 0
totalDuration = 400
endTime = totalDuration - totalDuration*.1 #this probably should be an equation that usues a totdur = .1(totdur)
random.seed(20) # 20
panMin = 0
panMax = 7

while x < totalDuration:
	direction = 101
	transposition = 50
	x += 1
	if 100 < x < 145:
		x = x + random.uniform(4, 8)
		searchTuple = ('germany', )
		probabilityPlay(x, direction, transposition, panMin, panMax, searchTuple)
	if 145 < x < 175:
		x = x + random.uniform(3, 6)
		searchTuple = ('belgium', )
		probabilityPlay(x, direction, transposition, panMin, panMax, searchTuple)
	if 175 < x < 210:
		searchTuple = ('tulip', )
		x = x + random.uniform(3, 5)
		probabilityPlay(x, direction, transposition, panMin, panMax, searchTuple)
	if 380 < x < 400:
		searchTuple = ('all', )
		x = x + random.uniform(.1, 2)
		probabilityPlay(x, direction, transposition, panMin, panMax, searchTuple)
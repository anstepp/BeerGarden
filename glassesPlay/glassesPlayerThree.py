#player number three
from rtcmix import *
import random
import math
from glassesSpectral import spectralPlay # start, amp, matrixMin, matrixMax, search

# comment/uncomment for routing to stereo source
#set_option("device = Soundflower (16ch)")

# set params call - change other module(s) if error
rtsetparams(44100, 8, 16)

# to write to file
#set_option("play = off", "clobber = on")
#rtoutput("/Users/anstepp/Desktop/glassesThree.aif")

# load - prevents some error
load("SPECTACLE2")

random.seed(20) # 20

x = 1

while x < 90:
	#do nothing
	x += 2
while 90 < x < 130:
	#play some spectral delay - Germany variation
	searchTuple = ('germany', )
	spectralPlay(x, 2, 5, 7, searchTuple)
	x += random.uniform(3, 7)
while 130 < x < 190:
	#do nothing
	x += 5
while 190 < x < 220:
	#play some spectral delay - belgian variation
	searchTuple = ('belgium', )
	spectralPlay(x, 3, 0, 7, searchTuple)
	x += random.uniform(1, 4)
while 220 < x < 300:
	x += 1	
while 300 < x < 330:
	searchTuple = ('canada', )
	spectralPlay(x, 5, 3, 5, searchTuple)
	x += random.uniform(2, 5)
while 330 < x < 500:
	searchTuple = ('all', )
	spectralPlay(x, 5.5, 0, 7, searchTuple)
	x += random.uniform(1, 4)
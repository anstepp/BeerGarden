from rtcmix import *
from glassesGran import granularGlasses
from probabilityPlay import probabilityPlay
from glassesSpectral import spectralPlay
import random

#comment/uncomment for stereo/home play
#set_option("device = Soundflower (16ch)")

load("GRANULATE")
load("TRANS")
load("SPECTACLE2")

rtsetparams(44100, 8)
rtoutput('/Users/aaronstepp/Desktop/circularMotion.aif')

start = 145
y = 0
x = 0

while 0 <= x <= 100:
	search = ('chimay', )
	matrixMin = matrixMax = directProb = transProb = x
	probabilityPlay(x, 100, 100, matrixMin, matrixMax, search)
	x += 1
while 100 <= x <= 145:
	search = ('all', )
	dur = 8
	X = x / 4
	Y = X + 4
	trans = random.uniform(-3, 3)
	granularGlasses(x, dur, trans, X, Y, search)
	x += 4
while 145 <= x <= 180:
	searchArray = ('all', )
	amplitude = 1
	matrixMin = matrixMax = x / 2
	spectralPlay(start, amplitude, matrixMin, matrixMax, searchArray)
	x += 2
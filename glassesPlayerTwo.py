#player number two
from rtcmix import *
import random
import math
from stereoInsurance import stereoInsurance 
#stereoInsurance(left, right, minPan, maxPan) where left and right are values 0-7
from glassesGran import granularGlasses 
# granularGlasses(start, dur, grainTrans, chanX, chanY, searchTuple)

# comment/uncomment for send to stereo
#set_option("device = Soundflower (16ch)")

rtsetparams(44100, 8)
load("GRANULATE")
#set_option("clobber = on", "play = off")
#rtoutput("/Users/anstepp/Desktop/glassesTwo.aif")

random.seed(400) # 400

x = 0
while x < 500:
	duration = 30
	if x < 20:
		minPan = 7
		maxPan = 9
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		searchTuple = ('weizen', )
		transposition = -3
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(6, 7)
	while 20 < x < 40:
		duration = 25
		minpan = 6
		maxPan = 10
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		searchTuple = ('snifter', )
		transposition = -2
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(5, 7)
	while 40 < x < 60:
		minPan = 0
		maxPan = 5
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		searchTuple = ('tulip', )
		transposition = -1
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(4, 7)
	while 60 < x < 80:
		maxPan = 6
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		searchTuple = ('chalice', )
		transposition = 0
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(4, 6)
	while 80 < x < 100:
		duration = 10
		maxPan = 7
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		searchTuple = ('all', )
		transposition = 1
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(3, 5)
	while 100 < x < 220:
		#do nothing
		x += 1
	while 220 < x < 310:
		duration = 5
		maxPan = 7
		searchTuple = ('all', )
		transposition = 2
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(4, 9)
	while 310 < x < 430:
		minPan = 3
		maxPan = 5
		searchTuple = ('all', )
		transposition = 3
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(4, 9)
	while 430 < x < 500:
		duration = 45
		minPan = 4
		maxPan = 6
		transposition = random.choice([-4, -3])
		searchTuple = ('all', )
		left = random.randint(minPan, maxPan)
		right = random.randint(minPan, maxPan)
		testVar,xChan,yChan = stereoInsurance(left, right, minPan, maxPan)
		if testVar is True:
			granularGlasses(x, duration, transposition, xChan, yChan, searchTuple)
		x += random.uniform(4, 9)
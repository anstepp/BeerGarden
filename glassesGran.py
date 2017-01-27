# graunlator for sung glasses
# it granulates...

# import functions
from rtcmix import *
import random
import math
from glassReader import fileReturn # fileReturn(searchTuple)
from stereo2oct import * #stereoToOct(x, y)

#rtsetparams(44100, 8)
load("GRANULATE")
load("FREEVERB")

def granularGlasses(start, dur, grainTrans, chanX, chanY, *args): 
#keep the *args last for the searchTuple
###file search and inTab assignment
	searchingTuple = ('sung', )
	stereoToOct(chanX, chanY)
	for arg in args:
		searchingTuple = searchingTuple + arg
	fileName = fileReturn(searchingTuple)
	rtinput(fileName)
	inTab = maketable("soundfile", "nonorm", 0, fileName)
###remaining vars
	inSkip = .5 # this may have to be a table look up from the file name
	amp = .75 * maketable("curve", 1000, 0,0,2, 500,.75,-2, 1000,0)
	numChan = 2
	inChan = 0
	traverse = random.uniform(.01, .000001)
	winStart = 5 # may need to be a look up
	winEnd = 10 # may need to be a look up
	hopTime = .009
	inJit = random.uniform(.4, .5)
	outJit = random.uniform(0, .2)
	grainDurMin = grainDurMax = hopTime * random.uniform(20, 40)
	grainAmpMin = grainAmpMax = 1
	#grainTrans = grainTrans * maketable("curve", "nonorm", 1000, 0,1.1,10, 1000,1.2) 
	# this can become interesting - glisson and other methods of granular synthesis
	grainTransJit = random.uniform(-.1, .1)
	seed = 1
	#pans between two channels - selected somewhere else
	panMin = maketable("curve", 1000, 0,0,2, 800,1)
	panMax = maketable("curve", 1000, 0,0,-2, 800,1)
	GRANULATE(start, inSkip, dur, amp, inTab, numChan, inChan, winStart, winEnd, 1, 
			  traverse, maketable("window", 1000, "hanning"), hopTime, inJit, outJit, 
			  grainDurMin, grainDurMax, grainAmpMin, grainAmpMax, grainTrans, 0, 
			  grainTransJit, seed, panMin, panMax)

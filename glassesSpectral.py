# spectral delay function for the Beer Glasses
# designed to do very coarse (16-64 bin) delay on
# recordings.

# the all important import statements
from rtcmix import *
import random
from glassReader import * # fileReturn(searchArray)
from circleToSpeakers import speakerConversion # (speakerVar)

#function
def spectralPlay(start, amplitude, matrixMin, matrixMax, searchArray):
	bussingMatrix = []
	for x in range(matrixMin, matrixMax+1):
		y = repr(speakerConversion(x))
		bussingMatrix.append("out " + y)
	bus_config("SPECTACLE2", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])	
	amp = amplitude * 5 * maketable("curve", 1000, 0,0,2, 130,.9,-2, 250,.75,1, 1000,0)
	searchArray += ('struck', )
	file = fileReturn(searchArray)
	print file
	rtinput(file)
	indur = DUR()
	ringdur = indur * 10
	fftlen = pickrand(16, 32, 64)
	delTabLen = eqtablen = winlen = fftlen * 4
	min = .5
	max = 3
	seed = 1
	fb1 = random.uniform(.5,.8)
	fb2 = random.uniform(.5,.8)
	fb3 = random.uniform(.5,.8)
	fb = maketable("line", delTabLen, 0,fb1, delTabLen/2,fb2, delTabLen,fb3)
	mindelfreq = 0
	maxdelfreq = 0
	mineqfreq = 0
	maxeqfreq = 0
	deltime = maketable("random", "nonorm", delTabLen, "even", min, max, seed)
	ienv = maketable("line", 1000, 0,0, 1,1, 19,.75, 20,0)
	oenv = maketable("curve", 1000, 0,1,0, 2,1,-1, 20,0)
	overlap = 1
	window = 0
	eq = maketable("line", "nonorm", eqtablen, 0,-90, 200,-20, 8000,-3, 22050,-6)
	panTab = maketable("line", 1000, 0,0, 1000,1)
	SPECTACLE2(start, 0, indur, amp, ienv, ringdur, fftlen, winlen, window, overlap, eq, 
			   deltime, fb, mineqfreq, maxeqfreq, mindelfreq, maxdelfreq, 0, 1, 0, panTab)
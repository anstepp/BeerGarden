# Playing function for Beer Glasses Piece - Aaron Stepp
# Has giant function to do lots of interesting things to beer glass recordings
# At this point (03102011) decides to play things forward or backwards and higher or lower 
# octave

#import functions - you need these, so don't delete or comment them
from rtcmix import * #cmix functions
import random #needed for all the fancy random functions
from glassReader import fileReturn # fileReturn([tupleToSearchWith])
from circleToSpeakers import speakerConversion # 1 var - speaker to convert

# probability function:
# directProb determines forward or backward play
# transProb is compared to random numbers 0-100
# if transProb is more, note is transposed down an octave
# therefore, the lower transProb is, the less likely transposition is
# same for directProb... but I should have put that first

def probabilityPlay(start, directProb, transProb, matrixMin, matrixMax, *args):
	amp = random.uniform(.5, .75)
	bussingMatrix = []
	for x in range(matrixMin, matrixMax+1):
		y = repr(speakerConversion(x))
		bussingMatrix.append("out " + y)
	bus_config("TRANS", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])
	searchingArray = ()
	for arg in args:
		searchingArray = searchingArray + arg
	directTestVar = random.randint(0, 100)
	transTestVar = random.randint(0, 100)
	if directProb > directTestVar: # forward play
		searchingArray = searchingArray + ('forward', )
		file = fileReturn(searchingArray)
		rtinput(file)
		print file
		duration = DUR()
		curveDur = duration * 10
		if transTestVar < transProb:
			bus_config("TRANS", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])
			TRANS(start, 0, duration * 2.1, amp, 0)
		elif transTestVar > transProb:
			bus_config("TRANS", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])
			TRANS(start, 0, duration * 2.1, amp, -1)
	if directProb < directTestVar: #reverse play
		searchingArray = searchingArray + ('reverse', )
		file = fileReturn(searchingArray)
		rtinput(file)
		print file
		duration = DUR()
		if transTestVar > transProb:
			bus_config("TRANS", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])
			TRANS(start, 0, duration, amp, 0)
		if transTestVar < transProb:
			bus_config("TRANS", "in 0-1", bussingMatrix[random.randrange(0, len(bussingMatrix))])
			TRANS(start, 0, duration * 2.1, amp, -1)

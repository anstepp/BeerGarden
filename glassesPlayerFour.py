import random
from random import choice
from rtcmix import *
import random
from probabilityPlay import probabilityPlay # (start, directP, transP, panMin, panMax, search)
from rhythmMachine import populateTheRhythm # (maximum, factorOfNotes)

# comment/uncomment for send to stereo
#set_option("device = Soundflower (16ch)")

rtsetparams(44100, 8, 16)
load("TRANS")
directionProb = 101
transProb = 75

#set_option("clobber = on", "play = off")
#rtoutput("/Users/anstepp/Desktop/glassesFour.aif")

random.seed(20) # 20

x = 0
z = 0
panMin = 0
panMax = 7

while x < 500:
	x += 1
	if x == 100:
		stepsToTake = populateTheRhythm(20, 2)
		for y in range(0, 20):
			search = ('germany', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		for z in range(20):
			search = ('kostritzer', )
			probabilityPlay(x + z, directionProb, transProb, panMin, panMax, search)
			x += stepsToTake[z]
			if z == 19:
				x = 145
	if x == 145:
		playTime = x
		stepsToTake = populateTheRhythm(20, 3)
		for y in range(0, 20):
			search = ('belgium', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		for z in range(len(stepsToTake)):
			search = ('corsendonk', )
			probabilityPlay(playTime, directionProb, transProb, panMin, panMax, search)
			playTime += stepsToTake[z]
			if z == (len(stepsToTake) - 1):
				x = 181
	if x == 181:
		panMin = 6
		panMax = 8
		for y in range(random.randint(20, 30)):
			search = ('england', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
			x = 183.2
	if x == 183.2:
		panMin = 1
		panMax = 3
		iterables = random.randint(18, 25)
		for y in range(iterables):
			search = ('noCOA', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
			if y == iterables - 1:
				x = 183.9
	if x == 183.9:
		playValue = 184
		playValueTwo = 184
		stepsToTake = populateTheRhythm(random.randint(21, 26), 2)
		stepsToTakeTwo = populateTheRhythm(random.randint(19, 20), 3)
		panMin = 5
		panMax = 7
		for y in range(random.randint(21, 29)):
			search = ('belgium', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		for z in range(len(stepsToTake)):
			search = ('trappistesRochefort', )
			panMin = panMax = z % 8
			probabilityPlay(playValue, directionProb, transProb, panMin, panMax, search)
			playValue += stepsToTake[z]
		for zz in range(len(stepsToTakeTwo)):
			search = ('goudenCarolus', )
			panMin = panMax = (zz % 8) * -1
			probabilityPlay(playValueTwo, directionProb, transProb, panMin, panMax, search)
			playValueTwo += stepsToTakeTwo[zz]
			if zz == (len(stepsToTakeTwo) -1):
				x = 220
	if x == 220:
		for y in range(random.randint(20, 25)):
			search = ('canada', )
			panMin = 5
			panMax = 8
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		x = 223
	if x == 223:
		for y in range(random.randint(12, 14)):
			search = ('usa', )
			panMin = 1
			panMax = 5
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		x = 228
	if x == 228:
		directionProb = 0
		transProb = 0
		iterables = random.randint(14, 21)
		for y in range(iterables):
			search = ('canada', )
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)	
			if y == iterables - 1:
					x = 380
	if x == 380:
		directionProb = 90
		transProb = 100
		for y in range(0, 20):
			search = ('all', )
			panMin = 0 + y % 2
			panMax = panMin + 2
			directionProb = 0
			transProb = 0
			probabilityPlay(x, directionProb, transProb, panMin, panMax, search)
		for z in range(17):
			stepsToTake = populateTheRhythm(17, 2)
			search = ('germany', )
			directionProb = 90
			probabilityPlay(x + z, directionProb, transProb, panMin, panMax, search)
			x += stepsToTake[z]
		for z in range(22):
			stepsToTake = populateTheRhythm(22, 3)
			search = ('belgium', )
			directionProb = 90
			probabilityPlay(x + z, directionProb, transProb, panMin, panMax, search)
			x += stepsToTake[z]
		for z in range(20):
			directionProb = 90
			stepsToTake = populateTheRhythm(20, 2)
			search = ('canada', )
			probabilityPlay(x + z, directionProb, transProb, panMin, panMax, search)
			x += stepsToTake[z]			
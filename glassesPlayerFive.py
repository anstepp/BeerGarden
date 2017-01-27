from rtcmix import *
from glassesGran import granularGlasses #(start, dur, grainTrans, chanX, chanY, *args)
import random

# comment/uncomment for send to stereo
#set_option("device = Soundflower (16ch)")

rtsetparams(44100, 8)
load("GRANULATE")

#set_option("clobber = on", "play = off")
#rtoutput("/Users/anstepp/Desktop/glassesFive.aif")

random.seed(20) #20

for x in range(0, 500):
	if x == 375:
		granularGlasses(x, 120, -2.33, 1, 5, ('footedAleGlass',  ))
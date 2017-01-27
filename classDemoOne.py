from rtcmix import *
from circleToSpeakers import speakerConversion
from probabilityPlay import probabilityPlay
from glassReader import fileReturn

#set_option("device = Soundflower (16ch)")
rtsetparams(44100, 8)
load("TRANS")
load("STEREO")

#globals
x = 0

while x < 100:
	file = fileReturn(('germany', 'forward'  ))
	rtinput(file)
	dur = DUR()
	MIX(x, 0, dur, 1, 0, 1)
	x += dur
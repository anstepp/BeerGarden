# a function that takes two arguments and turns them into an
# rtcmix bus_config statement and returns it for the GRANULATE instrument
# there's got to be a better way...

from rtcmix import *
import random
from circleToSpeakers import speakerConversion

def stereoToOct(x, y):
	if x == y:
		print 'two shared speakers'
		return 0
	else:
		a = speakerConversion(x)
		b = speakerConversion(y)
		one = "out %s" % (a, )
		two = "out %s" % (b, )
		bus_config("GRANULATE", one, two)
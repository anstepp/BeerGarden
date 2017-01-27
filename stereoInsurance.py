# to guarantee that the granular playing module doesn't pick two of the same speaker
# note the recursive bit - snazzy

import random
from circleToSpeakers import speakerConversion

def stereoInsurance(l, r, min, max):
	while l == r:
		l = random.randint(min, max)
		r = random.randint(min, max)
		stereoInsurance(l, r, min, max)
	else:
		return (True, l, r)
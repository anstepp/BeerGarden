#! /usr/bin/env python

# to use this make SURE that you've fixed your PYTHONPATH in your
# .profile to look for this:
# /Volumes/AARON/Cmix/sco/playFromHere/glassesPlay
# or where ever I put this in the end...

 
import sys
sys.path.append('/Users/aaronstepp/Documents/Compositions/24_BeerGarden/playFromHere/glassesPlay/')
print sys.path

from processorThrow import filePlayer

#from processorThrow import filePlayer #filePlayer(home, list)
#import random
#import math
#from glassReader import fileReturn
#import glassMasterArray

home = True

fileList = ("glassesPlayerOne.py", "glassesPlayerTwo.py", "glassesPlayerThree.py", 
			"glassesPlayerFour.py", "glassesPlayerFive.py")
filePlayer(home, fileList)

sys.exit()
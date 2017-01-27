# reading file for master array of glasses
# defines a function that will return a file to be played
# allows for a list to be fed in
# it's then converted to a set and compared to all the sets in the
# dictionary.  File names are concatenated to a tuple, then searched
# through and the function returns one file.

import random
from glassMasterArray import *

def fileReturn(*args):
	finalResults = []
	searchArray = ()
	for arg in args:
		searchArray = searchArray + arg
	for k in files.iterkeys():
		searchFiles = files[k]
		test = set(searchFiles) >= set(tuple(searchArray))
		if test is True:
			finalResults.append(k)
	print len(finalResults)
	return finalResults[random.randint(0, len(finalResults)-1)]
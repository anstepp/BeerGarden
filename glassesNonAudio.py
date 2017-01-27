from multiprocessing import *
import multiprocessing
import subprocess
import sys
import random
from glassMasterArray import *

"""conversion for 8 channels into a circle"""
def speakerConversion(x):
	speakerArray = [4, 1, 3, 7, 5, 6, 2, 0]
	x = x % 8
	return speakerArray[x]

"""will search a file for soundfiles meeting requirements"""
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
	return finalResults[random.randint(0, len(finalResults)-1)]
	
"""random rhythm generation module"""
def populateTheRhythm(max, factor):
	rhythmMatrix = []
	doubleList = (0.25, 0.5, 0.75)
	tripleList = (0.33, 0.66)
	quintList = (0.2, 0.4, 0.6, 0.8)
	septList = (0.142, 0.285, 0.428, 0.571, 0.714, 0.857)
	nonList = (0.111, 0.222, 0.333, 0.444, 0.555, 0.666, 0.777, 0.888, 0.999)
	if factor == 2 or factor % 2 == 0:
		for x in range(0, max):
			rhythmMatrix.append(random.choice(doubleList))
	elif factor == 3 or factor % 3 == 0:
		for x in range(0, max):
			rhythmMatrix.append(random.choice(tripleList))
	elif factor == 5:
		for x in range(0, max):
			rhythmMatrix.append(random.choice(quintList))
	elif factor == 7:
		for x in range(0, max):
			rhythmMatrix.append(random.choice(septList))
	elif factor == 9:
		for x in range(0, max):
			rhythmMatrix.append(random.choice(nonList))
	return rhythmMatrix
	
def stereoInsurance(l, r, min, max):
	while l == r:
		l = random.randint(min, max)
		r = random.randint(min, max)
		stereoInsurance(l, r, min, max)
	else:
		return (True, l, r)
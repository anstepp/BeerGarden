import random

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
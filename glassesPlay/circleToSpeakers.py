speakerArray = [4, 1, 3, 7, 5, 6, 2, 0]

def speakerConversion(x):
	x = x % 8
	return speakerArray[x]
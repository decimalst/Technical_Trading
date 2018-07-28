import numpy as np
def runningMeanFast(x, N):
	return np.convolve(x, np.ones((N,))/N)[(N-1):]
def testFunct():
	print "hi"
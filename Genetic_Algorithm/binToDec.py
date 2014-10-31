import numpy as np
def binToDec(s):
	length = len(s)
	x = 0
	for i in range(length):
		x = x + s[length-1-i]*np.power(2,length-1-i)
	return x

#  s = np.array([1,1,0,1,1])
#  print binToDec(s)


	
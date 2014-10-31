import numpy as np 
import random
import binToDec
import targetFunc
def fitness(ind):
	indNumbers = ind.shape[0]
	fValueList = []
	indLength = ind.shape[1]
	for i in range(indNumbers):
		
		# convert binary to decimal
		decimalX = binToDec.binToDec(ind[i,:]);
		
		# convert decimalX into interval [-1,2]
		xValue = -1.0 + decimalX*3/(np.power(2,indLength)-1)
		
		# print xValue
		fValueList.append(targetFunc.targetFunc(xValue))
	
	# compute culmulative probability
	fValue = np.array(fValueList)
	fSum = np.sum(fValue*fValue)
	ps = fValue*fValue/fSum
	p = []
	p.append(ps[0])
	for i in range(indNumbers-1):
		p.append(p[i]+ps[i+1])
	# print p

	return fValue,p





# s = np.round(np.random.rand(4,5))
# fitness(s)
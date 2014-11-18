
# Using SA to solve flowtime problem: Pi stands for the time spent on assembly line of workpiece i,
# and  P1 = 8, P2 = 18 ,P3 =5, P4 = 15,so how can we arrange processing order of the 4 workpiece so
# that the tatol flowtime is  minimum.


import numpy as np
import random
import math

def neighborhoodMove(_x,_debug):
	
	_xLenght  =  len(_x)
	_changePosition = random.sample([0,1,2,3],2)
	
	if _debug == True:
		print "The %d th workpiece and %d th workpiece are changed.\n"  \
		% (_changePosition[0]+1,_changePosition[1]+1)
	
	# for i in range(_xLenght):
	# 	_xNeighborhood.append(_x[i])
	_xNeighborhood = [i for i in _x]

	_temp = _xNeighborhood[_changePosition[0]]
	_xNeighborhood[_changePosition[0]] = _xNeighborhood[_changePosition[1]]
	_xNeighborhood[_changePosition[1]] = _temp

	if _debug == True:
		print "The neighborhood of ",_x,"is ",_xNeighborhood,'.\n'

	return _xNeighborhood
	

def objectFunc(_x, _P):
	
	_xLenght = len(_x)
	_timeSeq = []
	
	for i in range(_xLenght):
		_timeSeq.append(_P[_x[i]-1])
	
	# _xFunc = sum(np.array(_timeSeq)*np.array([4,3,2,1]))
	_xFunc = np.inner(np.array(_timeSeq),np.array([4,3,2,1]))
	
	return _xFunc
	

def movementDeci(_x,_xNeighborhood,_currentT,_P,_debug):

	_xFunc = objectFunc(_x,_P)
	_xNeighFunc = objectFunc(_xNeighborhood,_P)
	
	_deltaFunc = _xNeighFunc - _xFunc
	

	if _xNeighborhood < 0:
		_decision = True
	else:
		if math.exp(-_deltaFunc / _currentT) > np.random.rand():
			_decision = True
		else:
			_decision = False

	if _debug == True:
		print "The object function of",_x,"is",_xFunc,".\n"
		print "The object function of",_xNeighborhood,"is",_xNeighFunc,".\n"
		if _decision == True:
			print "The movement is accepted, ,and new solution is",_xNeighborhood,".\n"
		else:
			print "The movement is denied,and current solution",_x,"is kept.\n"

	return _decision

initialT = 100
initialSol = list(np.random.permutation([1,2,3,4]))
finalT = 1
deltaT = 0.8
maxInnerLoop = 10

currentT = initialT
currentSol = initialSol
P =[8,18,5,15]

debug = True

while currentT > 1:

	if debug == True:
		print "#"*80
		print "The temperature is: ",currentT
	for i in range(maxInnerLoop):
		
		if debug == True:
			print "\n\nDuring %d th loop \n" %(i+1)
		neighborhood = neighborhoodMove(currentSol,debug)
		
		decision = movementDeci(currentSol,neighborhood,currentT,P,debug)
		
		if decision == True:
			currentSol = neighborhood
		
		currentT = currentT * deltaT
print "*"*80
print "The finial solution is %s ,and object value is %f. " %(currentSol,objectFunc(currentSol,P))
	
# x = [2,1,3,4]
# P = [8,18,5,15]

# timeSeq = objectFunc(x,P)
# print timeSeq
# x = np.random.permutation([1,2,3,4])

# neighborhood = neighborhoodMove(x)
# print x 

# print neighborhood

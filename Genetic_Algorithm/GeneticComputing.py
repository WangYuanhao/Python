import numpy as np 

def probOfCompute(p):
	test = np.zeros((1,100))
	l = round(100*p)
	test[0.0:l] = 1
	n = round(np.random.rand()*99)
	_computingPro = test[0,n]
	return _computingPro
	


def crossover(ind,selectN,pc):
	indLength = ind.shape[1]
	_scro = np.zeros((2,indLength))
	_computingPro = probOfCompute(pc)
	if computingPro == 1:
		chb = round(np.random.rand()*(indLength))+1
		_scro[0,:] = np.append(ind[selectN[0],0:chb],/
			        ind[selectN[1],chb:indLength])
		_scro[1,:] = np.append(ind[selectN[1],0:chb],/
		        ind[selectN[0],chb:indLength])
	else:
		_scro[0,:] = ind[selectN[0],:]
		_scro[1,:] = ind[selectN[1],:]

	return _scro


def mutation(snew,probOfmutaion):
	indLength = snew.shape[1]
	_snnew = snew
	_computingPro = probOfCompute(probOfmutaion) 
	if _computingPro == 1:
		chb = round(np.random.rand()*(indLength-1))
		_snnew[chb] = abs(snew[chb]-1)
	return _snnew



			
		


	
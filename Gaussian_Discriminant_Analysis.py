import numpy as np
import Gaussian_Distribution as GD
import scipy.stats as scstat
#import os
#######################################################################
#------------------------reading data from txt------------------------
#######################################################################
#path = '.'
#txtfiles = [item for item in os.listdir(path)
#	if item.endswith('.txt')]

#for filename in txtfiles:
trainingMatrix_0 = GD.readingData('trainingSet_0.txt')
trainingMatrix_1 = GD.readingData('trainingSet_1.txt')
dimension = trainingMatrix_0.shape[1] - 1
#trainingMatrix = np.vstack((trainingMatrix_0,trainingMatrix_1))
#print trainingMatrix_0
#print trainingMatrix_1
#print trainingMatrix

########################################################################
#--------------------implementation of GDA------------------------------
########################################################################
mean0 = np.mean(trainingMatrix_0[:,0:dimension], axis = 0)
mean1 = np.mean(trainingMatrix_1[:,0:dimension], axis = 0)
sigma0 = np.cov(trainingMatrix_0[:,0:dimension].T)
sigma1 = np.cov(trainingMatrix_1[:,0:dimension].T)

mu = float(len(trainingMatrix_0) )/ float(len(trainingMatrix_0) + len(trainingMatrix_1))
#print mu
testingMatrix_0 = GD.readingData('testingSet_0.txt')
#print len(testingMatrix_0)
testingMatrix_1 = GD.readingData('testingSet_1.txt')
testingMatrix = np.vstack((testingMatrix_0,testingMatrix_1))
outputLabel = np.zeros((len(testingMatrix),2))
for i in range(len(testingMatrix)):
	outputLabel[i,0] = i + 1
	p0 = scstat.multivariate_normal.pdf(testingMatrix[i,0:2],mean0,sigma0) *  mu/(scstat.multivariate_normal.pdf(testingMatrix   				[i,0:2],mean0,sigma0)*mu + scstat.multivariate_normal.pdf(testingMatrix[i,0:2],mean1,sigma1)*(1-mu))
	if p0 > 0.5:
		outputLabel[i,1] = 0
	else:
		outputLabel[i,1] = 1
errorRate = abs(outputLabel[:,1] - testingMatrix[:,2]).sum()/float(len(testingMatrix))

print "Error rate of GDA simulation:",errorRate

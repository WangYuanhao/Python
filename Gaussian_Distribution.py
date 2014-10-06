from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy
import scipy.stats as stacmp
import matplotlib.pyplot as plt
#######################################################################
# -----------------generate multivariate normal samples---------------
# #####################################################################
def generateSample(mean,sigma):

	# generate 100 samples
	np.random.seed(100)
	randomVar = np.random.multivariate_normal(mean,sigma,100)

	x = np.arange(min(randomVar[:,0]),max(randomVar[:,0]),0.01)
	y = np.arange(min(randomVar[:,1]),max(randomVar[:,1]),0.01)
	rndX1,rndY1 = np.meshgrid(x,y)

	#print  rndX.shape
	rndX = np.reshape(rndX1,(np.size(rndX1),1))
	rndY = np.reshape(rndY1,(np.size(rndY1),1))

	#print np.size(rndX)

	rndXY = np.append(rndX,rndY,axis=1)
	rndVarProb = stacmp.multivariate_normal.pdf(
	                rndXY,mean,sigma)

	#print rndVarProb.T
	#print np.size(rndVarProb)

	rndVarProb = np.reshape(rndVarProb,(len(y),len(x)))
	return randomVar,rndX1,rndY1,rndVarProb

#print rndVarProb
#print rndVarProb.shape
###################################################################
#----------------write data to txt--------------------------------
##################################################################
def writingData(filename,randomVar):
	fOpen = open(filename,'w')
	for records in randomVar:
		writingStr = "	".join(str(record) for record in records)
		fOpen.write(writingStr+'\n')
	fOpen.close()
###################################################################
#----------------------read data from txt--------------------------
###################################################################
def readingData(filename):
	fOpen = open(filename,'r')
	recordsInString = fOpen.readlines()
	rows = len(recordsInString)
	cols = len(recordsInString[0].strip.split('\t'))
	recordMatrix = zeros((rows,cols))
	index = 0
	for record in recordsInString:
		recordList = record.strip().split('\t')
		recordMatrix[index,:] = recordList
		index = index + 1
	fOpen.close()
	return recordMatrix
##################################################################
#-------------------Simulation---------------------------------
##################################################################
mean1 = [2,2]
sigma1 = [[1,0],[0,1]]

mean2 = [6,6]
sigma2 = [[1,0],[0,1]]

randomVar1,rndX1,rndY1,rndVarProb1 = generateSample(mean1,sigma1)
randomVar2,rndX2,rndY2,rndVarProb2 = generateSample(mean2,sigma2)

writingData('outputData_1.txt',randomVar1)
writingData('outputData_2.txt',randomVar2)


##################################################################
#----------------------plot figure--------------------------------
##################################################################
#fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(rndX1,rndY1,rndVarProb)
# plt.show()
plt.contour(rndX1,rndY1,rndVarProb1)
plt.plot(randomVar1[:,0],randomVar1[:,1],'ro')

plt.contour(rndX2,rndY2,rndVarProb2)
plt.plot(randomVar2[:,0],randomVar2[:,1],'bo')
plt.grid(True)
plt.title('Simulation of Gaussian Distribution')
plt.show()
plt.savefig('simulationFig.png')




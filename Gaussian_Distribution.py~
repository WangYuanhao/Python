from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import scipy
import scipy.stats as stacmp
import matplotlib.pyplot as plt
mean = [1,1]
sigma = [[1,0],[0,1]]
#######################################################################
# -----------------generate multivariate normal samples---------------
# #####################################################################
def generateSample(mean,sigma):

	# generate 100 samples
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

randomVar,rndX1,rndY1,rndVarProb = generateSample(mean,sigma)

##################################################################
#----------------------plot figure--------------------------------
##################################################################
#fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot_surface(rndX1,rndY1,rndVarProb)
# plt.show()
plt.contour(rndX1,rndY1,rndVarProb)
plt.plot(randomVar[:,0],randomVar[:,1],'ro')
plt.show()
##################################################################
#----------------write data to txt--------------------------------
##################################################################
fOpen = open('outputData.txt','w')
for records in randomVar:
	writingStr = "	".join(str(record) for record in records)
	fOpen.write(writingStr+'\n')
fOpen.close()


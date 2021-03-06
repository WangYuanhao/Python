import numpy as np
import selection as sel
import fitness
import GeneticComputing as GC

import binToDec
import matplotlib.pyplot as plt
# length of individuals
indLength = 22
# size of initial population
indNumbers = 50
# max generations
gnmax = 200
probOfCrossover = 0.75
probOfMutaion = 0.05

population = np.round(np.random.rand(indNumbers,indLength))
scnew = np.zeros((indNumbers,indLength))
scnnew = np.zeros((indNumbers,indLength))
ymax = []
ymean = []
xmax = []

(f,p) = fitness.fitness(population)

gn = 1
while gn < gnmax+1:
	tempIndex = [index for index in range(indNumbers)]
	for i in tempIndex[0:indNumbers:2]:
		 # make selection,parents can be selected repeatedly
		 selectN = sel.selection(p)

         # crossover
		 scro = GC.crossover(population,selectN,probOfCrossover)
		 scnew[i,:] = scro[0,:]
		 scnew[i+1,:] = scro[1,:]

		 # mutation
		 scnnew[i,:] = GC.mutation(scnew[i,:],probOfMutaion)
		 scnnew[i+1,:] = GC.mutation(scnew[i+1,:],probOfMutaion)

	# new population
	population = scnnew

	(f,p) = fitness.fitness(population)
	fMax = f.max()

	# index of max value
	nMax = f.argmax()

	fMean = f.mean()

	ymax.append(fMax)
	ymean.append(fMean)
	x = binToDec.binToDec(population[nMax,:])
	xx = -1.0 + x*3/(np.power(2,indLength)-1)
	xmax.append(xx)
	gn = gn + 1

gn = gn - 1



plt.subplot(2,1,1)
plt.plot(np.linspace(1,200,200),np.array(ymax),label="max fitness")
plt.plot(np.linspace(1,200,200),np.array(ymean),label="mean of fitness")
plt.title('change of fitness according to generations')
plt.legend(loc = 9)

plt.subplot(2,1,2)
plt.plot(np.linspace(1,200,200),np.array(xmax),'r-',label='variation')
plt.legend(loc = 8)

plt.savefig('GAImage.jpg')
print 'The best fitness=',ymax[indNumbers-1]
print 'The best individuals=',xmax[indNumbers-1]

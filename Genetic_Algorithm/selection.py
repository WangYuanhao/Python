import numpy as np
def selection(p):
	# select two individuals at a time

	# indNumbers = ind.shape[0]
	selectN = []
	for i in range(2):
		r = np.random.rand()
		prand = np.array(p) - r
		j  = 0
		while prand[j]<0:
			j = j + 1
		
		selectN.append(j)
	

	return selectN
	

# p = [0.097779649410858635, 0.40546164518498468, 0.91093908098772136, 1.0]
# selectN = selection(p)
# print selectN
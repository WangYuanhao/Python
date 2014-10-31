import numpy as np
# import matplotlib.pyplot as plt 
def targetFunc(x):
	f = x * np.sin(10*np.pi*x) + 2
	return f

# x = np.linspace(-5,5,1000)
# funcValue = targetFunc(x)
# plt.plot(x,funcValue)
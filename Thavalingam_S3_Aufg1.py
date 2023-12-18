import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1e-3, 100, 1e-3)

def f(x): 
    return 5/(2*(x**(2/3)))

plt.grid()
plt.figure(1)
plt.loglog(x, f(x), label = 'f(x)')
plt.legend()
plt.show()    
    

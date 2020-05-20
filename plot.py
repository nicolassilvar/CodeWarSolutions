import matplotlib.pyplot as plt
import numpy as np


#set x,y scales to log log
plt.xscale('log')
plt.yscale('log')

t = np.linspace(2,100,num = 100)

plt.plot(t, 8*t,
t, 4*t*np.log(t),
t, 2*np.power(t,2),
t, np.power(t,3),
t, np.power(2,t)
)
plt.show()
prnt()

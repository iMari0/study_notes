import numpy as no
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10,20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

r = np.corrcoef(x,y)
#plot the data points
plt.plot(x,y,'o')
#define slope and intercept
m,b = np.polyfit(x,y,1)
plt.plot(x, m*x+b)
plt.show()
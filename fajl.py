import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.001)
y = ((x**2)+(x**3))/(4*x)

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

ax.set_aspect("equal")
# plot the function
ax.plot(x,y, 'r')
ax.grid()

# show the plot

plt.show()
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
f = "x**2"

def plotmaker(user_input:str,size:int):
    x = np.arange(-size,size,0.0001)
    y = eval(user_input)
    return [x,y]


to_plt = plotmaker(f,10)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.set_aspect("equal")
# plot the function
ax.plot(to_plt[0],to_plt[1], 'r')
ax.grid()
#ax.set_yticks([x for x in range(-20,20,4)])
#ax.set_xticks([x for x in range(-20,20,4)])
ax.set_ylim(0,10)
ax.axis("equal")

# show the plot

plt.show()
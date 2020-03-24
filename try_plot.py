import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure

fig = plt.figure()
x = plt.subplot()
x.scatter(12,11)
x.plot([[1,2,3,4,5,6],[7,8,9]],[[6,5,4,3,2,1],[4,3,2]])
plt.show()
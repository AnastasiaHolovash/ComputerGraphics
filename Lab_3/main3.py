from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import math
import numpy

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)
"""
X = []
Y = []
Z = []

for t in numpy.arange(0.0, 2 * math.pi, 0.5):
    for u in numpy.arange(0.0, math.pi, 0.5):
        tempX = math.sin(t) * math.cos(u)
        X.append(tempX)
        tempY = math.sin(t) * math.sin(u)
        Y.append(tempY)
        Z.append(math.sqrt(pow(tempX, 2) + pow(tempY, 2)))
"""
print(X)
print(Y)
print(Z)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()

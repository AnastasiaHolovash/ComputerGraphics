import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

from mpl_toolkits.mplot3d.axes3d import get_test_data
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# set up a figure twice as wide as it is tall
fig = plt.figure(figsize=plt.figaspect(0.5))

# ===============
#  First subplot
# ===============
# set up the axes for the first plot
ax = fig.add_subplot(1, 2, 1, projection='3d')

# plot a 3D surface like in the example mplot3d/surface3d_demo
u, v = np.mgrid[0:2*np.pi:30j, 0:2*np.pi:30j]
x = np.sin(u)*np.cos(v)
#x = np.arange(-1, 1, 0.25)
y = np.sin(u)*np.sin(v)
z = np.sqrt(x**2 + y**2)


# X = np.arange(-5, 5, 0.25)
# print(X)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

# fig2 = plt.figure(figsize=plt.figaspect(0.5))
# ax2 = fig2.add_subplot(1, 2, 1, projection='3d')
# u, v = np.mgrid[0:2*np.pi:30j, 0:2*np.pi:30j]
# x = np.sin(u)*np.cos(v)
# y = np.sin(u)*np.sin(v)
# z = np.arange(0.4, 0.5, 0.01)
#
# surf2 = ax2.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
# ax2.set_zlim(-1.01, 1.01)
# fig2.colorbar(surf2, shrink=0.5, aspect=10)

plt.show()

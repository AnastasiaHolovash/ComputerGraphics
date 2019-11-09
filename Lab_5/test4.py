import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

TWOPI = 2*np.pi

fig, ax = plt.subplots()

t = np.arange(0.0, TWOPI, 0.01)
x = t * np.sin(t)
y = t * np.cos(t)
l = plt.plot(x, y)

ax = plt.axis(xlim=(-50, 50), ylim=(-50, 50))

redDot, = plt.plot([0], [np.sin(0)], 'ro')

def animate(i):
    redDot.set_data(i, np.sin(i))
    return redDot,


# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames=500,
                                      interval=40, blit=True, repeat=True)

plt.show()
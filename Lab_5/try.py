import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import fabs
import random

# # First trajectory
# t1 = np.arange(0, 500, 0.01)
# x1 = t1 * np.sin(t1)
# y1 = t1 * np.cos(t1)
# trajectory1 = plt.plot(x1, y1)
#
# # Second trajectory
# t2 = np.arange(0, 500, 0.01)
# x2 = t2 * np.sin(t2) + 6
# y2 = t2 * np.cos(t2) + 6
# trajectory2 = plt.plot(x2, y2)

plt.style.use('dark_background')

# fig = plt.figure
fig, ax = plt.subplots()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line1, = ax.plot([], [], lw=2, color='blue')
line2, = ax.plot([], [], lw=2, color='violet')
ball1, = ax.plot([], [], color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=33)
ball2, = ax.plot([], [], color='violet', marker='o', linestyle='dashed', linewidth=2, markersize=33)


# Функция инициализации.
def init():
    # создение пустого графа.
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2,


xdata, ydata = [], []
xdata2, ydata2 = [], []

# Color for random choosing
colors = ['white', 'yellow', 'red', 'brown', 'blue', 'violet', 'orange']


# функция анимации
def animate(i):
    t = 0.1 * i
    tt = 0.2 * i

    print(i)

    # x, y данные на графике

    # First trajectory
    x1 = t * np.sin(tt)
    y1 = t * np.cos(tt)

    bx1 = t * np.sin(tt)
    by1 = t * np.cos(tt)

    # Second trajectory
    x2 = t * np.sin(t) + 10
    y2 = t * np.cos(t) + 6

    bx2 = (t * np.sin(t)) + 10
    by2 = (t * np.cos(t)) + 6

    # добавление новых точек в список точек осей x, y
    xdata.append(x1)
    ydata.append(y1)
    line1.set_data(xdata, ydata)

    ball1.set_data(bx1, by1)

    xdata2.append(x2)
    ydata2.append(y2)
    line2.set_data(xdata2, ydata2)

    ball2.set_data(bx2, by2)

    difference_x = fabs(x1 - x2) * 10
    difference_y = fabs(y1 - y2) * 10

    # print(difference_x, "\n", difference_y)

    if (difference_x < 100 and difference_y < 100):
        new_color = colors[random.randint(0, len(colors)-1)]
        ball1.set_data(color=new_color)
        ball2.set_data(color=new_color)

        print("YES")

    return line1, line2, ball1, ball2


# Заголовок анимации
plt.title('Lab_5')
# Скрываем лишние данные
plt.axis('off')

# Вызов анимации.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=70, blit=True)

plt.show()

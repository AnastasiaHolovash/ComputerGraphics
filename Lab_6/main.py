import tkinter as tk
import math
import time


def s(x, y, z, dist):
    return 1 / 2 + x * dist / (z + dist) + 500, 1 / 2 - y * dist / (z + dist) + 500


def matrfor_x(x, y, z, fi):
    return x, y * math.cos(fi) - z * math.sin(fi), y * math.sin(fi) + z * math.cos(fi)


def matrfor_y(x, y, z, fi):
    return x * math.cos(fi) + z * math.sin(fi), y, -x * math.sin(fi) + z * math.cos(fi)


def matrfor_z(x, y, z, fi):
    return x * math.cos(fi) - y * math.sin(fi), x * math.sin(fi) + y * math.cos(fi), z


def drawFigure(a, b):
    h = (a * math.sqrt(3)) / 2
    S1 = (0, -b, 0)
    S2 = (0, 0, 0)

    A = (a / 2, 0, -h)
    B = (-a / 2, 0, -h)
    C = (-a / 2, -b, -h)
    D = (a / 2, -b, -h)
    A1 = (a / 2, 0, -h - a)
    B1 = (-a / 2, 0, -h - a)
    C1 = (-a / 2, -b, -h - a)
    D1 = (a / 2, -b, -h - a)

    a = [B, S2, S1, C, B, A, S2, S1, D, A, A1, B1, B, C, D, D1, C1, C, C1, B1, A1, D1]
    return a

root = tk.Tk()
root.geometry("1000x1000")
canv = tk.Canvas(root, bg='white', width=1000, height=1000)
dist = 1000
canv.place(x=0, y=0)
j = 0

while True:
    j += 1
    canv.delete(j - 1)
    a = drawFigure(100, 200)
    for i in range(len(a)):
        # a[i] = matrfor_x(a[i][0], a[i][1], a[i][2], j / 100)  # X
        a[i] = matrfor_y(a[i][0], a[i][1], a[i][2], j / 100)  # Y
        # a[i] = matrfor_z(a[i][0], a[i][1], a[i][2], j / 100)  # Z
        a[i] = s(a[i][0], a[i][1], a[i][2], dist)
    canv.create_line(a)
    canv.update()
    time.sleep(0.05)
root.mainloop()

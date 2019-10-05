import tkinter as tk
import math
import argparse
from Lab_1.romb import Romb as model


def main(n, m, colors_n, colors_m):
    window = tk.Tk()
    window.title("Lab 1")

    sise = 1

    # Romb 1
    vd_1 = 175 * sise   # vertical diagonal 1
    hd_1 = 400 * sise   # horizontal diagonal 1

    # Romb 2
    vd_2 = 175 * sise  # vertical diagonal 2
    hd_2 = 175 * sise   # horizontal diagonal 2

    # coordinates of the start point
    x = 100
    y = 200

    coords = [
        hd_1, vd_1, (x, y)
    ]

    mdl = model(*coords)
    some = mdl.get_center_coord()

    coords2 = [
        hd_2, vd_2, ((some[0] - hd_2/2) / 1, (some[1] - vd_2) / 1)
        #hd_2, vd_2, (400, 400)
    ]

    mdl2 = model(*coords2)
    canv = tk.Canvas(window, width=900, height=900)

    colors_n = ["Purple", "lightpink"]
    #"""
    for angle in [math.pi / m * i for i in range(-m, m)]:
        mdl2.create_square(
            canv, angle, colors_n[0], center=False)
    #"""
    for angle in [math.pi / n * i for i in range(-n, n)]:
        mdl.create_square(
            canv, angle, colors_n[1], center=True)
    #"""
    window.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Built different charts with sqaures acording to params')
    parser.add_argument(
        '--n', help='Initialize num for center rotation', type=int, default=100)
    parser.add_argument(
        '--m', help='Initialize num for corner rotation', type=int, default=90)
    parser.add_argument(
        '--colors_inner', help='Initialize colors for center rotation',
        type=str, default=['black', 'black'], nargs=2)
    parser.add_argument(
        '--colors_outer', help='Initialize colors for corner rotation',
        type=str, default=['black', 'black'], nargs=2)

    args = parser.parse_args()
    main(args.n, args.m, args.colors_inner, args.colors_outer)

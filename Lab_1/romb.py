import math


class Romb:
    def __init__(self, d1: int, d2: int, startPoint: tuple):
        self.d1 = d1
        self.d2 = d2
        self.startPoint = startPoint

    def get_coord(self) -> tuple:
        a1 = self.startPoint[0] + (self.d1 / 2), self.startPoint[1]
        a2 = self.startPoint[0] + (self.d1), self.startPoint[1] + (self.d2 / 2)
        a3 = self.startPoint[0] + (self.d1 / 2), self.startPoint[1] + (self.d2)
        a4 = self.startPoint[0], self.startPoint[1] + (self.d2 / 2)
        return a1, a2, a3, a4

    def get_center_coord(self) -> tuple:
        x = self.startPoint[0] + (self.d1 / 2)
        y = self.startPoint[1] + (self.d2 / 2)
        return x, y

    def _transform(self, x: tuple, y: tuple, center: tuple, angle: float) -> tuple:
        x -= center[0]
        y -= center[1]

        temp_x = x * math.cos(angle) - y * math.sin(angle)
        temp_y = x * math.sin(angle) + y * math.cos(angle)

        return temp_x + center[0], temp_y + center[1]

    def rotate(self, angle: float, center=True) -> list:
        center = (self.get_coord()[2], self.get_center_coord())[center]

        rotated_coords = [
            self._transform(x, y, center, angle) for x, y in self.get_coord()
        ]

        return rotated_coords


    def create_square(
            self, canv, angle: float, color: str,
            center: bool = True
    ):
        m = self.rotate(angle, center=center)

        canv.create_line(m[0][0], m[0][1], m[1][0], m[1][1], fill=color)
        canv.create_line(m[1][0], m[1][1], m[2][0], m[2][1], fill=color)

        canv.create_line(m[2][0], m[2][1], m[3][0], m[3][1], fill=color)
        canv.create_line(m[0][0], m[0][1], m[3][0], m[3][1], fill=color)

        canv.pack()

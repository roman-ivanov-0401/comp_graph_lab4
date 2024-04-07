from OpenGL.GLU import *
import math


class Camera:
    def setup(self, x, y, z, ah, av):
        self._x = x
        self._y = y
        self._z = z
        self._ah = ah
        self._av = av
        self.turn_h(2)
        self.turn_v(1)

    def __init__(self):
        self._x = 0
        self._y = 0
        self._z = 0
        self._dx = 0
        self._dy = 0
        self._dz = 0
        self._ah = 0
        self._av = 0
        self._step = 0.2
        self._dah = 0.04
        self._dav = 0.04
        self.setup(80, 5, 80, 0, 0)

    def look_at(self):
        gluLookAt(
            self._x,
            self._y,
            self._z,
            self._x + self._dx,
            self._y + self._dy,
            self._z + self._dz,
            0, 1, 0
        )

    def turn_h(self, direction: float):
        self._ah += direction * self._dah
        self._dx = math.sin(self._ah)
        self._dz = -1 * math.cos(self._ah)

    def turn_v(self, direction):
        if not (abs(self._av + direction * self._dav) >= math.pi / 4):
            self._av += direction * self._dav
            self._dy = math.sin(self._av)

    def move(self, direction: float):
        self._x += direction * self._dx
        self._y += direction * self._dy
        self._z += direction * self._dz

    def step_h(self, direction: float):
        self._x += direction * self._step
        self._z += direction * self._step

    def step_v(self, direction: float):
        self._y += direction * self._step

    def print(self):
        pass

from OpenGL.GL import *
from utils import cross_prod

class House:
    def __init__(self, position, size):
        self._x = position[0]
        self._y = position[1]
        self._z = position[2]
        self._size = size / 100
        self._roof_color = (66, 48, 34)
        self._base_color = (237, 193, 121)
        self._door_color = (168, 41, 19)
        self._window_color = (10, 180, 242)
        self._window_frame_thickness = 2.0

    def _draw_glass(self, x_delta, y_delta):
        glNormal(0, 0, 1)
        glVertex3f(42.86 - self._window_frame_thickness + x_delta, 28.57 + self._window_frame_thickness + y_delta, 93.0)
        glVertex3f(28.58 + (self._window_frame_thickness / 2) + x_delta, 28.57 + self._window_frame_thickness + y_delta, 93.0),
        glVertex3f(28.58 + (self._window_frame_thickness / 2) + x_delta, 42.86 - (self._window_frame_thickness / 2) + y_delta, 93.0),
        glVertex3f(42.86 - self._window_frame_thickness + x_delta, 42.86 - (self._window_frame_thickness / 2) + y_delta, 93.0),

    def _draw_front_window(self):
        glColor3ub(*self._roof_color)
        glBegin(GL_QUADS)

        # Рамка
        glNormal(0, 0, 1)
        glVertex3f(14.29, 28.57, 92.9)
        glVertex3f(42.86, 28.57, 92.9)
        glVertex3f(42.86, 57.14, 92.9)
        glVertex3f(14.29, 57.14, 92.9)

        # Стёкла

        glColor3ub(*self._window_color)
        x_delta = -1 * (14.28 - (self._window_frame_thickness / 2))
        y_delta = 14.28 - (self._window_frame_thickness / 2)
        self._draw_glass(0, 0)
        self._draw_glass(x_delta, 0)
        self._draw_glass(x_delta, y_delta)
        self._draw_glass(0, y_delta)

        glEnd()

    def _draw_door(self):
        glColor3ub(*self._door_color)
        glBegin(GL_QUADS)

        glNormal(0, 0, 1)
        glVertex3f(85.71, 0.0, 92.9)
        glVertex3f(64.29, 0.0, 92.9)
        glVertex3f(64.29, 42.86, 92.9)
        glVertex3f(85.71, 42.86, 92.9)

        glEnd()

    def _draw_roof(self):
        glColor3ub(*self._roof_color)
        glPushMatrix()
        glTranslate(0, 0.25, 0)
        glBegin(GL_QUADS)

        # Перед
        glNormal(0, 0, 1)
        glVertex3f(100, 64.29, 100)
        glVertex3f(100, 74.29, 100)
        glVertex3f(50, 100, 100)
        glVertex3f(50, 92.86, 100)

        glNormal(0, 0, 1)
        glVertex3f(50, 100, 100)
        glVertex3f(50, 92.86, 100)
        glVertex3f(0.0, 64.29, 100)
        glVertex3f(0.0, 74.29, 100)

        # Верх
        glNormal(*cross_prod([-50, 25.71, 0], [0, 0, 100]))
        glVertex3f(100, 74.29, 0.0)
        glVertex3f(100, 74.29, 100.0)
        glVertex3f(50.0, 100.0, 100.0)
        glVertex3f(50.0, 100.0, 0.0)

        glNormal(*cross_prod([0, 0, 100], [50, 25.71, 0]))
        glVertex3f(0, 74.29, 0.0)
        glVertex3f(0, 74.29, 100.0)
        glVertex3f(50.0, 100.0, 100.0)
        glVertex3f(50.0, 100.0, 0.0)

        # Зад

        glNormal(0, 0, -1)
        glVertex3f(100, 64.29, 0)
        glVertex3f(100, 74.29, 0)
        glVertex3f(50, 100, 0)
        glVertex3f(50, 92.86, 0)

        glNormal(0, 0, -1)
        glVertex3f(50, 100, 0)
        glVertex3f(50, 92.86, 0)
        glVertex3f(0.0, 64.29, 0)
        glVertex3f(0.0, 74.29, 0)

        # Низ

        glVertex3f(100, 64.29, 100)
        glVertex3f(100, 64.29, 0)
        glVertex3f(50, 92.86, 0)
        glVertex3f(50, 92.86, 100)

        glVertex3f(0, 64.29, 100)
        glVertex3f(0, 64.29, 0)
        glVertex3f(50, 92.86, 0)
        glVertex3f(50, 92.86, 100)

        # Бока

        glNormal(1, 0, 0)
        glVertex3f(100, 74.29, 100)
        glVertex3f(100, 64.29, 100)
        glVertex3f(100, 64.29, 0)
        glVertex3f(100, 74.29, 0)

        glNormal(-1, 0, 0)
        glVertex3f(0, 74.29, 100)
        glVertex3f(0, 64.29, 100)
        glVertex3f(0, 64.29, 0)
        glVertex3f(0, 74.29, 0)

        glEnd()
        glPopMatrix()

        glColor3ub(*self._base_color)

        glBegin(GL_TRIANGLES)

        glNormal(0, 0, 1)
        glVertex3f(92.86, 68.57, 92.86)
        glVertex3f(50, 92.86, 92.68)
        glVertex3f(7.14, 68.57, 92.86)

        glNormal(0, 0, -1)
        glVertex3f(92.86, 68.57, 0.0)
        glVertex3f(50, 92.86, 0.0)
        glVertex3f(7.14, 68.57, 0.0)

        glEnd()

    def _draw_base(self):
        glColor3ub(*self._base_color)
        glBegin(GL_QUADS)

        # Перед
        glNormal(0, 0, 1)
        glVertex3f(92.86, 0, 92.86)
        glVertex3f(92.86, 68.57, 92.86)
        glVertex3f(7.14, 68.57, 92.86)
        glVertex3f(7.14, 0, 92.86)

        # Бока

        glNormal(1, 0, 0)
        glVertex3f(92.86, 0, 92.86)
        glVertex3f(92.86, 68.57, 92.86)
        glVertex3f(92.86, 68.57, 0)
        glVertex3f(92.86, 0, 0)

        glNormal(-1, 0, 0)
        glVertex3f(7.14, 68.57, 92.86)
        glVertex3f(7.14, 0, 92.86)
        glVertex3f(7.14, 0, 0.0)
        glVertex3f(7.14, 68.57, 0.0)

        # Зад
        glNormal(0, 0, -1)
        glVertex3f(92.86, 0, 0.0)
        glVertex3f(92.86, 68.57, 0.0)
        glVertex3f(7.14, 68.57, 0.0)
        glVertex3f(7.14, 0, 0.0)

        # Пол
        glVertex3f(92.86, 0, 92.86)
        glVertex3f(92.86, 0, 7.14)
        glVertex3f(7.14, 0, 7.14)
        glVertex3f(7.14, 0, 92.86)

        glEnd()

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslate(self._x, self._y, self._z)
        glScale(self._size, self._size, self._size)
        self._draw_roof()
        self._draw_base()
        self._draw_door()
        self._draw_front_window()
        glPopMatrix()


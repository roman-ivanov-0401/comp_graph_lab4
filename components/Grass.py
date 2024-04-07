from OpenGL.GL import *


class Grass:
    def __init__(self, height):
        self._height = height
        self._color = (25, 209, 25)
        # self._color = (100, 100, 100)

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glColor3ub(*self._color)
        glBegin(GL_QUADS)

        glNormal(0, 1, 0)
        glVertex3f(-100.0, self._height, -100.0)
        glVertex3f(-100.0, self._height, 100.0)
        glVertex3f(100.0, self._height, 100.0)
        glVertex3f(100.0, self._height, -100.0)

        glEnd()

        glPopMatrix()

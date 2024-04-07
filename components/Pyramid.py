from OpenGL.GL import *


class Pyramid:
    def __init__(self, start_position, size):
        self._x = start_position[0]
        self._y = start_position[1]
        self._z = start_position[2]
        self._size = size / 100

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glEnable(GL_DEPTH_TEST)
        glTranslate(self._x, self._y, self._z)
        glScale(self._size, self._size, self._size)

        glBegin(GL_TRIANGLES)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-50.0, 0, -86.6)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-50.0, 0, 86.6)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(100, 0, 0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-50.0, 0, -86.6)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-50.0, 0, 86.6)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0, 100, 0)

        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-50.0, 0, -86.6)
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(100, 0, 0)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0, 100, 0)

        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(100, 0, 0)
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-50.0, 0, 86.6)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(0, 100, 0)
        glEnd()
        glDisable(GL_DEPTH_TEST)

        glPopMatrix()

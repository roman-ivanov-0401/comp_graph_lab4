import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from utils import cross_prod


class Projector:
    def __init__(self, position, angle, direction, light_color, number_of_light):
        self.position = position
        self.angle = angle
        self.direction = direction
        self.light_color = light_color
        self.number_of_light = number_of_light

    def draw(self):

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glTranslate(*self.position)
        start_direction = [0.0, 0.0, 1.0]
        cross = cross_prod(start_direction, self.direction)
        dir_norm = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2 + self.direction[2] ** 2)
        rot_angle = math.asin(1 / dir_norm)
        glRotate(rot_angle / math.pi * 180 + 180, *cross)
        glColor3f(1.0, 0.0, 0.0)
        glutSolidCone(1, 3, 20, 20)
        glColor3f(1.0, 1.0, 0.0)
        glutSolidSphere(.7, 7, 7)
        glLightfv(self.number_of_light, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
        glLightfv(self.number_of_light, GL_DIFFUSE, self.light_color)
        glLightfv(self.number_of_light, GL_POSITION, [1, 0, 0, 1.0])
        # glLightfv(self.number_of_light, GL_SPOT_DIRECTION, self.angle)
        glPopMatrix()

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.Floor import Floor
from components.Pyramid import Pyramid
from Camera import Camera


def reshape_handler(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    f_aspect = width / height
    gluPerspective(45.0, f_aspect, 1.0, 800.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def remove_handlers():
    glutReshapeFunc(None)
    glutKeyboardFunc(None)
    glutSpecialFunc(None)


# def timer_handler(value):
#     glutPostRedisplay()
#     glutTimerFunc(8, timer_handler, 1)


class Task1(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.floor = Floor(5, -1, (1.0, 0.0, 1.0), (0.0, 0.0, 0.0))
        self.camera = Camera()
        self.pyramid = Pyramid((0.0, 0.0, 0.0), 10.0)

    def set_handlers(self):
        def special_key_handler(key, *args):
            match key:
                case 100:
                    self.camera.turn_h(-1)
                case 102:
                    self.camera.turn_h(1)
                case 101:
                    self.camera.turn_v(1)
                case 103:
                    self.camera.turn_v(-1)
            glutPostRedisplay()

        def keyboard_handler(key, *args):
            match key:
                case b'w':
                    self.camera.move(1)

                case b's':
                    self.camera.move(-1)

                case b'a':
                    self.camera.step_h(-1)

                case b'd':
                    self.camera.step_h(1)

            glutPostRedisplay()

        glutReshapeFunc(reshape_handler)
        glutSpecialFunc(special_key_handler)
        glutKeyboardFunc(keyboard_handler)
        # glutTimerFunc(8, timer_handler, 1)

    def on_mount(self):
        self.set_handlers()
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

    def on_unmount(self):
        remove_handlers()
        glShadeModel(GL_FLAT)
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.camera.look_at()
        self.floor.draw()
        self.pyramid.draw()

        glutSwapBuffers()

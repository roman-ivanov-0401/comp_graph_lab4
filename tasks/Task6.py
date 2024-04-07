from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.Floor import Floor
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
    # glutTimerFunc(8, None, 1)
    glutSpecialFunc(None)


def timer_handler(value):
    glutPostRedisplay()
    glutTimerFunc(8, timer_handler, 1)


class Task6(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.floor = Floor(5, -1, (1.0, 0.0, 1.0), (0.0, 0.0, 0.0))
        self.camera = Camera()

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

        def keyboard_handler(key, *args):
            key = key.decode('UTF-8')
            match key:
                case 'w':
                    self.camera.move(1)

                case 's':
                    self.camera.move(-1)

                case 'a':
                    self.camera.step_h(-1)

                case 'd':
                    self.camera.step_h(1)

            glutPostRedisplay()

        glutReshapeFunc(reshape_handler)
        glutKeyboardFunc(keyboard_handler)
        glutTimerFunc(8, timer_handler, 1)
        glutSpecialFunc(special_key_handler)




    def on_mount(self):
        self.set_handlers()
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

    def on_unmount(self):
        remove_handlers()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # gluLookAt(
        #     *(-49.92, 0.039, -50.996),
        #     *(-49.84, 0.079, -51.993),
        #     *(0, 1, 0))

        self.camera.look_at()
        self.floor.draw()

        glutSwapBuffers()

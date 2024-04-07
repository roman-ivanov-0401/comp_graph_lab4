from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.Grass import Grass
from Camera import Camera
from components.House import House


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


class Task4(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.grass = Grass(0)
        self.camera = Camera()
        self.house = House([0, 0, 0], 15)
        self.ambient_color = [.5, .5, .5, 1.0]
        self.diff_position = [100.0, 100.0, 100.0, 1.0]
        self.diff_color = [.5, .5, .5, 1.0]
        self.specular = [0.1, 0.1, 0.1, 1.0]
        self.specref = [.1, .1, .1, 1.0]

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

    def _init_light(self):
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.ambient_color)
        glLightfv(GL_LIGHT0, GL_POSITION, self.diff_position)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.diff_color)

    def on_mount(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, self.specref)
        glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, 128)
        glEnable(GL_LIGHT0)


        self.set_handlers()
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

    def on_unmount(self):
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_LIGHT0)

        remove_handlers()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        self._init_light()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.camera.look_at()
        self.grass.draw()
        self.house.draw()


        glutSwapBuffers()

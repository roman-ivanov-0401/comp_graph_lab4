from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.Grass import Grass
from Camera import Camera
from components.Projector import Projector
from components.House import House

menu_points = [
    {
        "name": "Первый прожектор",
        "number": 0,
        "submenu": [
            {
                "name": "Красный",
                "number": 0
            },
            {
                "name": "Зелёный",
                "number": 1
            },
            {
                "name": "Синий",
                "number": 2
            },
            {
                "name": "Белый",
                "number": 3
            },
            {
                "name": "Фиолетовый",
                "number": 4
            },
        ]
    },
    {
        "name": "Второй прожектор",
        "number": 1,
        "submenu": [
            {
                "name": "Красный",
                "number": 0
            },
            {
                "name": "Зелёный",
                "number": 1
            },
            {
                "name": "Синий",
                "number": 2
            },
            {
                "name": "Белый",
                "number": 3
            },
            {
                "name": "Фиолетовый",
                "number": 4
            },
        ]
    }
]

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


class Task5(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.menu = None
        self.grass = Grass(0)
        self.camera = Camera()
        self.proj1 = Projector([0, 20, 0], 20, [0, -1, 0], [1.0, 0.0, 0.0, 1.0], GL_LIGHT0)
        self.proj2 = Projector([0, 60, 0], 70, [0, -1, 0], [0.0, 0.0, 1.0, 1.0], GL_LIGHT1)
        self.house = House([0, 0, 0], 15)
        self.sky_blue = (13.5 / 256, 20.6 / 256, 23.5 / 256, 1.0)

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

    def _init_menu(self):
        def first_menu_handler(option):
            pass

        def second_menu_handler(option):
            pass

        def menu_handler(option):
            pass

        first_menu = glutCreateMenu(first_menu_handler)

        for i in range(5):
            glutAddMenuEntry(menu_points[0]["submenu"][i]["name"], menu_points[0]["submenu"][i]["number"])

        second_menu = glutCreateMenu(second_menu_handler)

        for i in range(5):
            glutAddMenuEntry(menu_points[1]["submenu"][i]["name"], menu_points[1]["submenu"][i]["number"])

        self.menu = glutCreateMenu(menu_handler)
        glutAddSubMenu(menu_points[0]["name"], first_menu)
        glutAddSubMenu(menu_points[1]["name"], second_menu)
        glutAttachMenu(GLUT_LEFT_BUTTON)

    def on_mount(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        self.set_handlers()
        self._init_menu()
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

    def on_unmount(self):
        remove_handlers()
        glDisable(GL_DEPTH_TEST)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHT1)
        glutDestroyMenu(self.menu)
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        glClearColor(*self.sky_blue)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.camera.look_at()
        self.grass.draw()
        self.house.draw()
        self.proj1.draw()
        self.proj2.draw()

        glutSwapBuffers()

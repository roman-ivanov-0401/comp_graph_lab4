from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.Grass import Grass
from Camera import Camera
from components.House import House

menuPoints = [
    {
        "name": "Первый источник",
        "number": 0,
        "submenu": [
            {
                "name": "Включить",
                "number": 0
            },
            {
                "name": "Выключить",
                "number": 1
            },
        ]
    },
    {
        "name": "Второй источник",
        "number": 0,
        "submenu": [
            {
                "name": "Включить",
                "number": 0
            },
            {
                "name": "Выключить",
                "number": 1
            },
        ]
    },
    {
        "name": "Третий источник",
        "number": 0,
        "submenu": [
            {
                "name": "Включить",
                "number": 0
            },
            {
                "name": "Выключить",
                "number": 1
            },
        ]
    },
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


class Task3(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.sky_blue = (13.5 / 256, 20.6 / 256, 23.5 / 256, 1.0)
        self.floor = Grass(0)
        self.camera = Camera()
        self.house = House((0, 0, 0), 15)
        self.ambient_colors = [[0.2, 0.0, 0.0, 1.0], [0.0, 0.2, 0.0, 1.0], [0.0, 0.0, 0.2, 1.0]]
        self.first_light_source = {
            "color": [1.0, 0.0, 0.0, 1.0],
            "position": [100.0, 5.0, 100.0, 0.0]
        }
        self.second_light_source = {
            "color": [0.0, 1.0, 0.0, 1.0],
            "position": [-100.0, 5.0, 100.0, 0.0]
        }
        self.third_light_source = {
            "color": [0.0, 0.0, 1.0, 1.0],
            "position": [-100.0, 5.0, -100.0, 0.0]
        }
        self.menu = None

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

    def _init_lights(self):
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.ambient_colors[0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.first_light_source["color"])
        glLightfv(GL_LIGHT0, GL_POSITION, self.first_light_source["position"])
        glLightfv(GL_LIGHT1, GL_AMBIENT, self.ambient_colors[1])
        glLightfv(GL_LIGHT1, GL_DIFFUSE, self.second_light_source["color"])
        glLightfv(GL_LIGHT1, GL_POSITION, self.second_light_source["position"])
        glLightfv(GL_LIGHT2, GL_AMBIENT, self.ambient_colors[2])
        glLightfv(GL_LIGHT2, GL_DIFFUSE, self.third_light_source["color"])
        glLightfv(GL_LIGHT2, GL_POSITION, self.third_light_source["position"])

    def _init_menu(self):
        def first_source_menu_handler(option):
            if option == 1:
                glDisable(GL_LIGHT0)
            else:
                glEnable(GL_LIGHT0)
            glutPostRedisplay()

        def second_source_menu_handler(option):
            if option == 1:
                glDisable(GL_LIGHT1)
            else:
                glEnable(GL_LIGHT1)
            glutPostRedisplay()

        def third_source_menu_handler(option):
            if option == 1:
                glDisable(GL_LIGHT2)
            else:
                glEnable(GL_LIGHT2)
            glutPostRedisplay()

        def menu_handler(option):
            pass

        first_source_menu = glutCreateMenu(first_source_menu_handler)

        glutAddMenuEntry(menuPoints[0]["submenu"][0]["name"], menuPoints[0]["submenu"][0]["number"])
        glutAddMenuEntry(menuPoints[0]["submenu"][1]["name"], menuPoints[0]["submenu"][1]["number"])

        second_source_menu = glutCreateMenu(second_source_menu_handler)

        glutAddMenuEntry(menuPoints[1]["submenu"][0]["name"], menuPoints[1]["submenu"][0]["number"])
        glutAddMenuEntry(menuPoints[1]["submenu"][1]["name"], menuPoints[1]["submenu"][1]["number"])

        third_source_menu = glutCreateMenu(third_source_menu_handler)

        glutAddMenuEntry(menuPoints[2]["submenu"][0]["name"], menuPoints[1]["submenu"][0]["number"])
        glutAddMenuEntry(menuPoints[2]["submenu"][1]["name"], menuPoints[1]["submenu"][1]["number"])

        self.menu = glutCreateMenu(menu_handler)
        glutAddSubMenu(menuPoints[0]["name"], first_source_menu)
        glutAddSubMenu(menuPoints[1]["name"], second_source_menu)
        glutAddSubMenu(menuPoints[2]["name"], third_source_menu)
        glutAttachMenu(GLUT_LEFT_BUTTON)

    def on_mount(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        self.set_handlers()

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glEnable(GL_LIGHT2)
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
        glDisable(GL_LIGHT2)
        glutDestroyMenu(self.menu)

        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        self._init_lights()
        glClearColor(*self.sky_blue)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.camera.look_at()
        self.floor.draw()
        self.house.draw()

        glutSwapBuffers()

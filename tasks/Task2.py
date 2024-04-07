from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks.Task import Task
from components.House import House
from components.Grass import Grass
from components.Floor import Floor
from Camera import Camera

menuPoints = [
    {
        "name": "Задать glLightModelfv",
        "number": 0,
        "submenu": [
            {
                "name": "Светлое освещение",
                "number": 0,
                "color": [1.0, 1.0, 1.0, 1.0]
            },
            {
                "name": "Тёмное освещение",
                "number": 1,
                "color": [0.3, 0.3, 0.3, 1.0]
            },
            {
                "name": "Красное освещение",
                "number": 2,
                "color": [1.0, 0.0, 0.0, 1.0]
            },
            {
                "name": "Синее освещение",
                "number": 3,
                "color": [0.0, 0.0, 1.0, 1.0]
            },
            {
                "name": "Зелёное освещение",
                "number": 4,
                "color": [0.0, 1.0, 0.0, 1.0]

            },
            {
                "name": "Фиолетовое освещение",
                "number": 5,
                "color": [0.5, 0.0, 1.0, 1.0]
            },
            {
                "name": "Черный",
                "number": 6,
                "color": [0.0, 0.0, 0.0, 1.0]
            },
        ]
    },
    {
        "name": "Задать glColorMaterial",
        "number": 1,
        "submenu": [
            {
                "name": "Согласование цветов",
                "number": 0,
                "color": [1.0, 1.0, 1.0, 1.0]
            },
            {
                "name": "Красный",
                "number": 1,
                "color": [1.0, 0.0, 0.0, 1.0]
            },
            {
                "name": "Зелёный",
                "number": 2,
                "color": [0.0, 1.0, 0.0, 1.0]
            },
            {
                "name": "Синий",
                "number": 3,
                "color": [0.0, 0.0, 1.0, 1.0]
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


def menu_handler(option):
    pass


class Task2(Task):
    def __init__(self, name: str, number: int):
        super().__init__(name, number)
        self.grass = Grass(0)
        self.camera = Camera()
        self.menu = None
        self.gl_light_model_fv_menu = None
        self.gl_color_material_menu = None
        self.house = House((0, 0, 0), 20)
        self.floor = Floor(5, 0, (255, 0, 0), (0, 255, 255))
        self.sky_blue = (135 / 256, 206 / 256, 235 / 256)
        self.ambient_color = [0.4, 0.4, 0.4, 1.0]

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
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_COLOR_MATERIAL)
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient_color)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glClearColor(*self.sky_blue, 1.0)

        def gl_light_model_fv_menu_handler(option):
            self.ambient_color = menuPoints[0]["submenu"][option]["color"]
            glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.ambient_color)
            glutPostRedisplay()

        def gl_color_material_menu_handler(option):
            if option == 0:
                glEnable(GL_COLOR_MATERIAL)
            else:
                glDisable(GL_COLOR_MATERIAL)
                glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, menuPoints[1]["submenu"][option]["color"])
            glutPostRedisplay()

        self.gl_light_model_fv_menu = glutCreateMenu(gl_light_model_fv_menu_handler)
        for point in menuPoints[0]["submenu"]:
            glutAddMenuEntry(point["name"], point["number"])

        self.gl_color_material_menu = glutCreateMenu(gl_color_material_menu_handler)
        for point in menuPoints[1]["submenu"]:
            glutAddMenuEntry(point["name"], point["number"])

        self.menu = glutCreateMenu(menu_handler)

        glutAddSubMenu("gl_light_model_fv", self.gl_light_model_fv_menu)
        glutAddSubMenu("gl_color_material", self.gl_color_material_menu)
        glutAttachMenu(GLUT_LEFT_BUTTON)

        self.set_handlers()

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

    def on_unmount(self):
        glClearColor(0.0, 0.0, 0.0, 0.3)

        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)
        glDisable(GL_DEPTH_TEST)

        glutDestroyMenu(self.menu)

        remove_handlers()

        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.camera.look_at()
        self.grass.draw()
        self.house.draw()

        glutSwapBuffers()

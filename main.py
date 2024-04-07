import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tasks import (
    Task1,
    Task2,
    Task3,
    Task4,
    Task5,
    Task6,
    Task7,
    Task8,
    Task9
)

tasks = [
    Task1.Task1("Задание №1", 0),
    Task2.Task2("Задание №2", 1),
    Task3.Task3("Задание №3", 2),
    Task4.Task4("Задание №4", 3),
    Task5.Task5("Задание №5", 4),
    Task6.Task6("Задание №6", 5),
    Task7.Task7("Задание №7", 6),
    Task8.Task8("Задание №8", 7),
    Task9.Task9("Задание №9", 8),
]

config = {
    "task_on_start": 0
}

state = {
    "current_menu_point": 0
}


def tasks_menu_handler(option):
    tasks[state["current_menu_point"]].on_unmount()
    glutDisplayFunc(tasks[option].display)
    tasks[option].on_mount()
    state["current_menu_point"] = option
    glutPostRedisplay()


def init_tasks_menu():
    menu = glutCreateMenu(tasks_menu_handler)
    for task in tasks:
        glutAddMenuEntry(task.name, task.number)
    glutAttachMenu(GLUT_RIGHT_BUTTON)


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(1000, 1000)
glutCreateWindow("Lab #4")
init_tasks_menu()
glutDisplayFunc(tasks[config["task_on_start"]].display)
tasks[config["task_on_start"]].on_mount()
glutMainLoop()

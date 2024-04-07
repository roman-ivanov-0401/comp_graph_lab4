import math
from OpenGL.GL import *


def cross_prod(a, b):
    result = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    result = [c / math.sqrt(result[0] ** 2 + result[1] ** 2 + result[2] ** 2) for c in result]
    return result


def cross_prod_without_norm(a, b):
    result = [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
    return result


print(GL_LIGHT0)
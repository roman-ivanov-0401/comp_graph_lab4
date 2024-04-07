from OpenGL.GL import *


class Floor:
    def __init__(self, size, y_coord, first_color, second_color):
        self.size = size
        self.y_coord = y_coord
        self.first_color = first_color
        self.second_color = second_color

    def draw(self):
        glBegin(GL_QUADS)
        for i in range((200 / self.size).__ceil__()):
            for j in range((200 / self.size).__ceil__()):
                glColor3f(*(self.first_color if (i + j) % 2 == 0 else self.second_color))
                glVertex3f(self.size * i - 100, self.y_coord, self.size * j - 100)
                glVertex3f(self.size * (i + 1) - 100, self.y_coord, self.size * j - 100)
                glVertex3f(self.size * (i + 1) - 100, self.y_coord, self.size * (j + 1) - 100)
                glVertex3f(self.size * i - 100, self.y_coord, self.size * (j + 1) - 100)
        glEnd()


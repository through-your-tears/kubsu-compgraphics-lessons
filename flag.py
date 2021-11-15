"""Флаг Пакистана OpenGL"""
from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import cos, sin, pi


def getX(centre, r, angle):
    return centre + r * cos(angle * pi / 180)


def getY(centre, r, angle):
    return centre + r * sin(angle * pi / 180)


def draw_circle(x, y, r):
    v = 100000  # чем больше число, тем выше точность прорисовки круга
    glBegin(GL_TRIANGLE_FAN)
    glVertex2d(x, y)
    for i in range(v):
        a = i / v * pi * 2
        glVertex2d(x + r * cos(a), y + r * sin(a))
    glEnd()


def draw_triangle(vertexes):
    glBegin(GL_TRIANGLES)
    for vertex in vertexes:
        glVertex2d(*vertex)
    glEnd()


def show():
    white = (1.0, 1.0, 1.0)
    green = (0.0, 0.25, 0.1)
    glClearColor(*green, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(*white)
    glBegin(GL_QUADS)
    quad_vertexes = [(-1, -1), (-1, 1), (-0.5, 1), (-0.5, -1)]
    for vertex in quad_vertexes:
        glVertex2d(*vertex)
    glEnd()
    draw_circle(0.2, 0, 0.5)
    glColor3f(*green)
    draw_circle(0.3, 0.1, 0.5)
    glColor3f(*white)
    rb = 0.2
    r = 0.075
    centre = (0.3, 0.2)
    for deg in range(0, 360, 72):
        tr_vertexes = [centre, (getX(centre[0], r, deg), getY(centre[1], r, deg)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)
        tr_vertexes = [centre, (getX(centre[0], r, deg + 72), getY(centre[1], r, deg + 72)),
                       (getX(centre[0], rb, deg + 36), getY(centre[1], rb, deg + 36))]
        draw_triangle(tr_vertexes)
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    window = glutCreateWindow("Pakistan flag")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()

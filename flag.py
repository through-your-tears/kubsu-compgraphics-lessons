"""Флаг Пакистана OpenGL"""
from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import cos, sin, pi


def getX(r, angle):
    return r * cos(angle * pi / 180)


def getY(r, angle):
    return r * sin(angle * pi / 180)


def draw_circle(x, y, r):
    v = 100000  # чем больше число, тем выше точность прорисовки круга
    glBegin(GL_TRIANGLE_FAN)
    glVertex2d(x, y)
    for i in range(v):
        a = i / v * pi * 2
        glVertex2d(x + r * cos(a), y + r * sin(a))
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
    draw_circle(0.1, -0.1, 0.5)
    '''
    glBegin(GL_POLYGON)
    deg1 = 18
    deg2 = 54
    rb = 0.5
    r = 0.2
    coords = [(0, rb), (getX(r, deg2), getY(r, deg2)), (getX(rb, deg1), getY(rb, deg1)),
              (getX(r, deg1), -getY(r, deg1)), (getX(rb, deg2), -getY(rb, deg2)), (0, -r),
              (-getX(rb, deg2), -getY(rb, deg2)),  (-getX(r, deg1), -getY(r, deg1)),
              (-getX(rb, deg1), getY(rb, deg1)), (-getX(r, deg2), getY(r, deg2))]
    for coord in coords:
        glVertex2d(*coord)
    glEnd()
    '''
    glColor3f(*green)
    draw_circle(0.2, 0, 0.5)
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutInitWindowPosition(50, 50)
window = glutCreateWindow("Pakistan flag")
glutDisplayFunc(show)
glutIdleFunc(show)
glutMainLoop()

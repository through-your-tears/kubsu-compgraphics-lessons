"""Флаг Пакистана OpenGL"""
from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import cos, sin


def show():
    glClearColor(0.0, 0.25, 0.1, 1.0)  # белый цвет на экране
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(3)
    glBegin(GL_QUADS)
    quad_vertexes = [(-1, -1), (-1, 1), (-0.5, 1), (-0.5, -1)]
    for vertex in quad_vertexes:
        glVertex2d(*vertex)
    glEnd()
    """
    glBegin(GL_TRIANGLE_FAN)
    v = 100
    glVertex2d(0.5, 0.1)
    for i in range(v):
        a = i / v * 3.1415 * 2
        glVertex2d(0.1 + 0.5 * cos(a), 0.1 + 0.5 * sin(a))
    glEnd()
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.25, 0.1)
    glVertex2d(0, 0)
    for i in range(v):
        a = i / v * 3.1415 * 2
        glVertex2d(0 + 0.4 * cos(a), 0 + 0.4 * sin(a))
    glEnd()
    """
    glBegin(GL_POLYGON)

    glEnd()

    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(50, 50)
window = glutCreateWindow("Pakistan flag")
glutDisplayFunc(show)
glutIdleFunc(show)
glutMainLoop()

"""Флаг Пакистана OpenGL"""
from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import cos, sin


def show():
    glClearColor(0.0, 0.25, 0.1, 1.0)  # зелёный цвет на экране
    glClear(GL_COLOR_BUFFER_BIT)

    glLineWidth(3)
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    quad_vertexes = [(-1, -1), (-1, 1), (-0.5, 1), (-0.5, -1)]
    for vertex in quad_vertexes:
        glVertex2d(*vertex)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    v = 10000
    glVertex2d(0.1, -0.1)
    for i in range(v):
        a = i / v * 3.1415 * 2
        glVertex2d(0.1 + 0.5 * cos(a), -0.1 + 0.5 * sin(a))
    glEnd()

    glBegin(GL_POLYGON)
    star_coords = []
    for i in range(11):
        star_coords.append(())
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.25, 0.1)
    glVertex2d(0.1, -0.1)
    for i in range(v):
        a = i / v * 3.1415 * 2
        glVertex2d(0.2 + 0.5 * cos(a), 0 + 0.5 * sin(a))
    glEnd()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(700, 700)
glutInitWindowPosition(50, 50)
window = glutCreateWindow("Pakistan flag")
glutDisplayFunc(show)
glutIdleFunc(show)
glutMainLoop()

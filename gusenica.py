from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *


def show():
    glBegin()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    window = glutCreateWindow("Gusenica")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()
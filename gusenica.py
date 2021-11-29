from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from panzer import rotate


def show():
    white = (1.0, 1.0, 1.0)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Gusenica")
    glutSpecialFunc(rotate)
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()
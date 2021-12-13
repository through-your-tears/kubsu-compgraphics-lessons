from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from light import light


def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotate(5, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(-5, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(5, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-5, 1, 0, 0)


def show():
    white = (1.0, 1.0, 1.0)
    green = (0.0, 1.0, 0.0)
    red = (1.0, 0.0, 0.0)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glLoadIdentity()
    glTranslatef(-0.5, 0, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, green)
    glutSolidTeapot(0.3)
    glTranslatef(1, 0, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, 6)
    glutSolidTeapot(0.3)
    glTranslatef(-0.5, 0, 0)

    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("teapots")
    glutDisplayFunc(show)
    glutSpecialFunc(rotate)
    light()
    glutMainLoop()


if __name__ == '__main__':
    main()
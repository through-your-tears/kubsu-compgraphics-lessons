from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *


global xrot
global yrot


def f():
    global xrot
    global yrot
    xrot = 0
    yrot = 0


def rotate(key, x, y):
    global xrot
    global yrot
    if key == GLUT_KEY_RIGHT:
        xrot += 5
    elif key == GLUT_KEY_LEFT:
        xrot -= 5
    elif key == GLUT_KEY_UP:
        yrot += 5
    elif key == GLUT_KEY_DOWN:
        yrot -= 5


def light():
    ambient = (1.0, 1.0, 1.0, 1)
    lightpos = [0, 1, 0, 0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


def show():
    global xrot
    global yrot
    white = (1.0, 1.0, 1.0)
    green = (0.0, 1.0, 0.0)
    red = (1.0, 0.0, 0.0)
    black = (0, 0, 0)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glLoadIdentity()
    glTranslatef(-0.5, 0, 0)
    glRotate(yrot, 0, 1, 0)
    glRotate(xrot, 0, 1, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, green)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 0)
    glutSolidTeapot(0.3)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glTranslatef(0.5, 0, 0)
    glRotate(yrot, 0, 1, 0)
    glRotate(xrot, 0, 1, 0)
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, red)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, white)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 8)
    glutSolidTeapot(0.3)
    glFlush()
    glutSwapBuffers()


def main():
    f()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("teapots")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(rotate)
    light()
    glutMainLoop()


if __name__ == '__main__':
    main()
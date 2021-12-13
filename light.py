from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from gusenica import draw_sphere
from gusenica import rotate


global ambient
global lightpos


def move_light(key, x, y):
    if key == GLUT_KEY_UP:
        if lightpos[1] <= 1:
            lightpos[1] += 0.1
    elif key == GLUT_KEY_DOWN:
        if lightpos[1] >= -1:
            lightpos[1] -= 0.1
    elif key == GLUT_KEY_LEFT:
        if lightpos[0] >= -1:
            lightpos[0] -= 0.1
    elif key == GLUT_KEY_RIGHT:
        if lightpos[0] <= 1:
            lightpos[0] += 0.1
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)
    glutPostRedisplay()


def light():
    global ambient
    global lightpos
    ambient = (1.0, 1.0, 1.0, 1)
    lightpos = [0, 0, 0, 0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)


def show():
    white = (1.0, 1.0, 1.0)
    black = (0, 0, 0)
    blue = (0.0, 0.0, 0.5)
    glClearColor(*black, 0.0)
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glColor3f(*blue)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, blue)
    draw_sphere(0.5, 50, 50)
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("light")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(move_light)
    # glutSpecialFunc(rotate)
    light()
    glutMainLoop()


if __name__ == '__main__':
    main()

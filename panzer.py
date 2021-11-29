from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from flag import draw_circle


def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotatef(-1, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(1, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(1, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-1, 1, 0, 0)


def draw_quad(vertexes):
    glBegin(GL_QUADS)
    for vertex in vertexes:
        glVertex2d(*vertex)
    glEnd()


def show():
    white = (1.0, 1.0, 1.0)
    any_green = (0.0, 0.5, 0.1)
    green = (0.0, 0.25, 0.1)
    black = (0.0, 0.0, 0.0)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(*black)
    quads_vertexes = [[(-0.4, 0.04), (-0.4, -0.16), (0.4, -0.2), (0.4, 0)],
                      [(0.4, 0), (0.4, -0.2), (0.5, -0.15), (0.5, 0.05)],
                      [(-0.4, 0.04), (-0.35, 0.1), (0.5, 0.1), (0.5, -0.01)]]
    for quad_vertexes in quads_vertexes:
        draw_quad(quad_vertexes)
        glColor3f(0.1, 0.1, 0.1)
    glColor3f(*green)
    quads_vertexes = [[(-0.3, 0.05), (-0.3, 0.27), (0.3, 0.25), (0.3, 0.02)],
                      [(0.3, 0.25), (0.3, 0.02), (0.35, 0.05), (0.35, 0.3)],
                      [(-0.3, 0.27), (-0.25, 0.3), (0.35, 0.3), (0.3, 0.25)]]
    for quad_vertexes in quads_vertexes:
        draw_quad(quad_vertexes)
        glColor3f(0.0, 0.4, 0.1)
    glColor3f(*any_green)
    quads_vertexes = [[(-0.2, 0.28), (-0.2, 0.38), (0.1, 0.37), (0.1, 0.27)],
                      [(0.1, 0.37), (0.1, 0.27), (0.15, 0.3), (0.15, 0.4)],
                      [(-0.2, 0.38), (-0.15, 0.41), (0.15, 0.4), (0.1, 0.37)]]
    for quad_vertexes in quads_vertexes:
        draw_quad(quad_vertexes)
        glColor3f(0.0, 0.3, 0.2)
    glColor3f(*black)
    quads_vertexes = [[(0.13, 0.32), (0.13, 0.36), (0.5, 0.35), (0.5, 0.31)],
                      [(0.5, 0.35), (0.5, 0.31), (0.51, 0.32), (0.51, 0.36)],
                      [(0.13, 0.36), (0.14, 0.37), (0.51, 0.36), (0.5, 0.35)]]
    for quad_vertexes in quads_vertexes:
        draw_quad(quad_vertexes)
        glColor3f(0.0, 0.1, 0.1)
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Panzer")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(rotate)
    glutMainLoop()


if __name__ == '__main__':
    main()

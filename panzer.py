from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from flag import draw_circle


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
    quad_vertexes = [(-0.6, 0), (-0.4, -0.2), (0.4, -0.2), (0.6, 0)]
    draw_quad(quad_vertexes)
    glColor3f(*green)
    quad_vertexes = [(-0.5, 0), (-0.4, 0.25), (0.2, 0.25), (0.5, 0)]
    draw_quad(quad_vertexes)
    glColor3f(*any_green)
    quad_vertexes = [(-0.2, 0.25), (-0.2, 0.35), (0.1, 0.35), (0.1, 0.25)]
    draw_quad(quad_vertexes)
    glColor3f(*black)
    quad_vertexes = [(0.1, 0.28), (0.1, 0.32), (0.5, 0.32), (0.5, 0.28)]
    draw_quad(quad_vertexes)
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(50, 50)
    window = glutCreateWindow("Panzer")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()
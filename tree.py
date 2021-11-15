from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from flag import draw_triangle


def show():
    white = (1.0, 1.0, 1.0)
    black = (0.0, 0.0, 0.0)
    green = (0.0, 0.25, 0.1)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    vertexes = [[-0.3, -0.5], [0.3, -0.5], [0, -0.1]]
    glColor3f(*green)
    height = 0.4
    delta_height = 0.4
    for i in range(3):
        draw_triangle(vertexes)
        vertexes[0][0] += 0.1
        vertexes[1][0] -= 0.1
        delta_height -= 0.1
        for j in range(2):
            vertexes[j][1] += height
        vertexes[2][1] += delta_height
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    window = glutCreateWindow("New Year tree")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutMainLoop()


if __name__ == '__main__':
    main()

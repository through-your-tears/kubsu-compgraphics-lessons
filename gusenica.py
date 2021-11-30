from OpenGL.GLUT import *
from OpenGL.GLE import *
from OpenGL.GL import *
from math import pi, sin, cos
from flag import draw_circle


def rotate(key, x, y):
    if key == GLUT_KEY_RIGHT:
        glRotate(-5, 0, 1, 0)
    elif key == GLUT_KEY_LEFT:
        glRotate(5, 0, 1, 0)
    elif key == GLUT_KEY_UP:
        glRotate(5, 1, 0, 0)
    elif key == GLUT_KEY_DOWN:
        glRotate(-5, 1, 0, 0)


def draw_sphere(r, nx, ny, mx=0, my=0, mz=0):
    dnx = 1.0 / nx
    dny = 1.0 / ny
    glBegin(GL_QUAD_STRIP)
    piy = pi * dny
    pix = pi * dnx
    for iy in range(ny):
        diy = iy
        ay = diy * piy
        sy = sin(ay)
        cy = cos(ay)
        ty = diy * dny
        ay1 = ay + piy
        sy1 = sin(ay1)
        cy1 = cos(ay1)
        ty1 = ty + dny
        for ix in range(nx):
            ax = 2.0 * ix * pix
            sx = sin(ax)
            cx = cos(ax)
            x = r * sy * cx
            y = r * sy * sx
            z = r * cy
            tx = ix * dnx
            glNormal3f(x + mx, y + my, z + mz)
            glTexCoord2f(tx, ty)
            glVertex3f(x + mx, y + my, z + mz)
            x = r * sy1 * cx
            y = r * sy1 * sx
            z = r * cy1
            glNormal3f(x + mx, y + my, z + mz)
            glTexCoord2f(tx, ty1)
            glVertex3f(x + mx, y + my, z + mz)
    glEnd()


def show():
    white = (1.0, 1.0, 1.0)
    green = (0.0, 0.25, 0.1)
    red = (1.0, 0.0, 0.0)
    glClearColor(*white, 1.0)
    glClear(GL_COLOR_BUFFER_BIT or GL_DEPTH_BUFFER_BIT)
    glColor3f(*green)
    move_list = [0, 0, 0]
    for i in range(5):
        draw_sphere(0.1, 40, 40, *move_list)
        for j in range(3):
            move_list[j] += 0.1
    glColor3f(*red)
    glMatrixMode(GL_PROJECTION)
    # move_list = [-0.01, -0.05, 0]
    # draw_sphere(0.01, 40, 40, *move_list)
    # move_list = [-0.05, -0.02, 0]
    # draw_sphere(0.01, 40, 40, *move_list)
    draw_circle(-0.06, -0.02, 0.01)
    draw_circle(0, -0.06, 0.01)
    glFlush()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Gusenica")
    glutDisplayFunc(show)
    glutIdleFunc(show)
    glutSpecialFunc(rotate)
    glutMainLoop()


if __name__ == '__main__':
    main()

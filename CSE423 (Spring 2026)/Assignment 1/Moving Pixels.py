from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 
import time



window_width, window_height = 1200, 600
spacebar_clicked =  False
transition_cycle = False
starting_time = None
points_coordinates = [] 
possible_directions = [(1,1), (-1,-1), (-1,1), (1, -1)]
pixel_moving_speed = 0.06



def draw_pixel():
    if spacebar_clicked: return 
    glPointSize(5)
    for i in range(len(points_coordinates)):
        x, y, r, g, b, _ = points_coordinates[i]
        if transition_cycle:
            time_spent = (time.time() - starting_time) % 1.0
            if time_spent <= 0.5:
                glColor3f(0,0,0)
            else:
                glColor3f(r,g,b)
        else:
            glColor3f(r,g,b)
        glBegin(GL_POINTS)
        glVertex2d(x,y)
        glEnd()                 



def create_pixels(button, state, x, y):
    global points_coordinates, transition_cycle, starting_time
    if spacebar_clicked : return 
    if button == GLUT_RIGHT_BUTTON  and state == GLUT_DOWN:
        limit = len(possible_directions)
        direction_index = random.randint(0, limit-1)
        random_direction = possible_directions[direction_index]
        glColor3f(random.random(), random.random(), random.random()) 
        convt_x, convt_y = x-(window_width/2), (window_height/2) - y
        points_coordinates.append([convt_x, convt_y, random.random(), random.random(), random.random(), random_direction])
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        transition_cycle = not transition_cycle
        starting_time = time.time() if transition_cycle else None
    glutPostRedisplay()



def speed_changer(key, x, y):
    global pixel_moving_speed
    if spacebar_clicked: return 
    if key == GLUT_KEY_UP :
        pixel_moving_speed += 0.02
    elif key == GLUT_KEY_DOWN:
        pixel_moving_speed = max(pixel_moving_speed - 0.02 , 0)

    glutPostRedisplay()



def moving_pixels():
    global  points_coordinates
    if spacebar_clicked: return 
    for i in range(len(points_coordinates)):
        j = points_coordinates[i]
        _,_,_,_,_, direction = j
        dir_x, dir_y = direction 
        j[0] += dir_x * pixel_moving_speed
        j[1] += dir_y * pixel_moving_speed
        if j[0] < -window_width // 2 or j[0] > window_width // 2 :
            dir_x *= -1
        if j[1] < -window_height // 2 or j[1] > window_height // 2:
            dir_y *= -1
        points_coordinates[i][5] = (dir_x, dir_y)
    glutPostRedisplay()



def pause_and_play(key, x, y):
    global spacebar_clicked
    if key == b' ':
        spacebar_clicked = not spacebar_clicked

    

def projections():
    glViewport(0, 0, window_width,  window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-window_width//2, window_width//2, -window_height // 2, window_height // 2 , 0, 1)
    glMatrixMode(GL_MODELVIEW)  
    


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    draw_pixel()    
    glutSwapBuffers()
    


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b"Moving Pixels")
    projections()
    glutDisplayFunc(display)
    glutMouseFunc(create_pixels)
    glutIdleFunc(moving_pixels)
    glutSpecialFunc(speed_changer)
    glutKeyboardFunc(pause_and_play)
    glutMainLoop()



if __name__ == "__main__":
    main()

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random
import copy

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 600
horizon_level = 0.7
house_center_x = 0.5
house_center_y = 0.5
bush_position = 0.55
rain_drop_size = 25
rain_drop_speed_min = rain_drop_size/3
rain_drop_speed_max = rain_drop_size/8
angle, max_angle, min_angle = 0, 15, -15
sky_r_day, sky_g_day, sky_b_day = 0.4, 0.7, 1
sky_r_night, sky_g_night, sky_b_night = 0, 0, 0
sky_r, sky_g, sky_b = sky_r_day, sky_g_day, sky_b_day
sky_color_change_speed = 0.002
night = False
rain_begin = [[i, WINDOW_HEIGHT, random.uniform(rain_drop_speed_min,rain_drop_speed_max), i] for i in range(0,WINDOW_WIDTH,8)]




def non_moving_objects():
    global sky_r, sky_g, sky_b
    # SKY
    glColor3f(sky_r, sky_g, sky_b)
    glBegin(GL_TRIANGLES)
    glVertex2f(WINDOW_WIDTH, 0)
    glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT)
    glVertex2f(0,0)
    glEnd()
    glColor3f(sky_r, sky_g, sky_b)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT)
    glVertex2f(0, WINDOW_HEIGHT)
    glEnd()

    # horizon

    glColor3f(145 / 255, 85 / 255, 55 / 255)
    glBegin(GL_TRIANGLES)
    glVertex2f(WINDOW_WIDTH, 0)
    glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT*horizon_level)
    glVertex2f(0,0)
    glEnd()
    glColor3f(145 / 255, 85 / 255, 55 / 255)
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT*horizon_level)
    glVertex2f(0, WINDOW_HEIGHT*horizon_level)
    glEnd()

    # bushes far behind house
    bush_base = 60

    for i in range(0, WINDOW_WIDTH, bush_base):
        glColor3f(81 / 255, 234 / 255, 66 / 255)
        glBegin(GL_TRIANGLES)
        glVertex2f(i,  WINDOW_HEIGHT*bush_position)
        glVertex2f(i+bush_base, WINDOW_HEIGHT*bush_position)
        glColor3f(31 / 255, 131 / 255, 21 / 255)
        glVertex2f(i + (bush_base/2), (WINDOW_HEIGHT * bush_position)+100)

        glEnd()


    # House
    X, Y  =  house_center_x * WINDOW_WIDTH, house_center_y * WINDOW_HEIGHT
    glColor3f(243 / 255, 176 / 255, 85 / 255)
    # House-left
    glBegin(GL_TRIANGLES)
    glVertex2f(X, Y)
    glVertex2f(X-200, Y + 100)
    glVertex2f(X - 200, Y - 100)
    glEnd()
    # House-right
    glBegin(GL_TRIANGLES)
    glVertex2f(X, Y)
    glVertex2f(X + 200, Y + 100)
    glVertex2f(X + 200, Y - 100)
    glEnd()
    # house-top
    glBegin(GL_TRIANGLES)
    glVertex2f(X, Y)
    glVertex2f(X + 200, Y + 100)
    glVertex2f(X - 200, Y + 100)
    glEnd()
    # house-bottom
    glBegin(GL_TRIANGLES)
    glVertex2f(X, Y)
    glVertex2f(X + 200, Y - 100)
    glVertex2f(X - 200, Y - 100)
    glEnd()

    # house top shadow
    glColor3f(199 / 255, 145 / 255, 72 / 255)
    glLineWidth(25)
    glBegin(GL_LINES)
    glVertex2f(X-200, Y+100)
    glVertex2f(X + 200, Y + 100)
    glEnd()

    # House Roof
    glColor3f(110 / 255, 77 / 255, 14 / 255)
    glBegin(GL_TRIANGLES)
    glVertex2f(X + 200 + 50, Y + 100 )
    glVertex2f(X , Y + 100 + 150)
    glColor3f(70 / 255, 49 / 255, 10 / 255)
    glVertex2f(X - 200 - 50, Y + 100 )
    glEnd()

    # House Door
    glColor3f(110 / 255, 77 / 255, 14 / 255)
    glLineWidth(100)
    glBegin(GL_LINES)
    glVertex2f(X, Y-100)
    glColor3f(52 / 255, 37 / 255, 8 / 255)
    glVertex2f(X, Y + 40)
    glEnd()

    # House Windows
    # Left Window
    glColor3f(74 / 255, 155 / 255, 205 / 255)
    glLineWidth(80)
    glBegin(GL_LINES)
    glVertex2f(X-130, Y+30)
    glColor3f(153 / 255, 213 / 255, 255 / 255)
    glVertex2f(X-130, Y-30)
    glEnd()
    glColor3f(0, 0, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(X-130, Y+30)
    glVertex2f(X-130, Y-30)
    glEnd()
    glColor3f(0, 0, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(X-130-40, Y)
    glVertex2f(X-130+40, Y)
    glEnd()
    # Right Window
    glColor3f(74 / 255, 155 / 255, 205 / 255)
    glLineWidth(80)
    glBegin(GL_LINES)
    glVertex2f(X+130, Y+30)
    glColor3f(153 / 255, 213 / 255, 255 / 255)
    glVertex2f(X+130, Y-30)
    glEnd()
    glColor3f(0, 0, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(X+130, Y+30)
    glVertex2f(X+130, Y-30)
    glEnd()
    glColor3f(0, 0, 0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(X+130-40, Y)
    glVertex2f(X+130+40, Y)
    glEnd()




def rain():
    global angle, max_angle, rain_begin
    glColor3f(0.8, 0.9, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    for j in range(len(rain_begin)):
            i = rain_begin[j]
            glVertex2f(i[0]-angle,i[1])
            glVertex2f(i[0]+angle,i[1]-rain_drop_size)

    glEnd()




def animate_rain():
    global angle, max_angle, rain_begin
    for j in range(len(rain_begin)):
        i = rain_begin[j]
        i[1] = i[1] - i[2]
        if angle > 0:

            i[0] = i[0] + i[2]

        elif angle < 0:

            i[0] = i[0] - i[2]

        if i[1] <= 0:
             i[1] = WINDOW_HEIGHT
             i[0] = i[3]
        if i[0] > WINDOW_WIDTH:
             i[0] = 0
        elif i[0] < 0:
             i[0] = WINDOW_WIDTH
        
    glutPostRedisplay()




def rain_direction_changer(special_key,a,b):
    global angle, max_angle, min_angle
    if special_key == GLUT_KEY_RIGHT :

        angle += 7.5 if (angle<max_angle) else 0
        print("Rain drops directed to the right")

    elif special_key == GLUT_KEY_LEFT:

        angle -= 7.5 if (angle>min_angle) else 0
        print("Rain drops directed to the left")

    glutPostRedisplay()





def animate_day_night():
    global sky_color_change_speed
    global night
    global sky_r, sky_g, sky_b
    global sky_r_night, sky_g_night, sky_b_night
    global sky_r_day, sky_g_day, sky_b_day

    i,j,k = sky_r, sky_g, sky_b
    if night:
                if i>sky_r_night:
                    i-=sky_color_change_speed
                if j>sky_g_night:
                    j-=sky_color_change_speed
                if k>sky_b_night:
                    k-=sky_color_change_speed

    else:
                if i<sky_r_day:
                    i+=sky_color_change_speed
                if j<sky_g_day:
                    j+=sky_color_change_speed
                if k<sky_b_day:
                    k+=sky_color_change_speed

    sky_r, sky_g, sky_b  = i, j, k
    glutPostRedisplay()




def day_night(keyboard_key, a, b):
    global night
    global sky_r, sky_g, sky_b
    global sky_r_night, sky_g_night, sky_b_night
    global sky_r_day, sky_g_day, sky_b_day
    if keyboard_key == b'd':
        night = True
        print("Night")
    elif keyboard_key == b'l':
        night = False
        print("Day")
    glutPostRedisplay()




def animation():
     animate_rain()
     animate_day_night()
     glutPostRedisplay()




def projection():
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)
    glMatrixMode(GL_MODELVIEW)




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    projection()
    non_moving_objects()
    rain()

    glutSwapBuffers()




def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Rain and House")

    glutDisplayFunc(display)
    glutIdleFunc(animation)
    glutSpecialFunc(rain_direction_changer)
    glutKeyboardFunc(day_night)
    glutMainLoop()




if __name__ == "__main__":
    main()

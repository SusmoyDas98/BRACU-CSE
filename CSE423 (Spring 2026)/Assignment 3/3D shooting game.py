from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random 
# from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_18

camera_pos = (800, -800, 700)
camera_look_at = (0,0,50)
axis_decision = (0, 0, 1)
window_height, window_width = 800, 1000
field_of_view = 55
GRID_LENGTH, GRID_WIDTH = 650, 650
rand_var = 423 

# debug mode controller
debug_mode = False

class Game:
    def __init__(self):
        self.first_person_mode = False
        self.player_body_height = 15
        self.player_head_radius = 10
        self.player_leg_height = 20
        self.player_leg_max_radius = 5
        self.player_width = 25
        self.player_speed = 10
        self.gun_height = 35
        self.player_spawn_coordinate = (100, 60, 0)
        self.enemies_spwan_coordinate = []
        self.enemy_radius = self.player_body_height*1.5
        self.enemy_jiggle_speed = 0.05
        self.enemy_expand = False
        self.gun_facing = ""
        self.player_angle = 0
        self.bullet_size = 2
        self.bullet_fired = False
        self.bullet_speed = 1
        self.bullets = []
        self.isAlive = True

        for i in range(5):
            self.enemy_locations()

    def enemy_locations(self):

        x = self.player_spawn_coordinate[0]
        y = self.player_spawn_coordinate[1]        
        while True:
            val_x = random.randint(int(-GRID_WIDTH//2+self.enemy_radius), int(GRID_WIDTH//2-self.enemy_radius))
            val_y = random.randint(int(-GRID_WIDTH//2+self.enemy_radius), int(GRID_WIDTH//2-self.enemy_radius))
            if (val_x, val_y) != (x, y) and (val_x, val_y) not in self.enemies_spwan_coordinate:
                self.enemies_spwan_coordinate.append((val_x, val_y, self.enemy_radius))
                break                    

    def reset_camera(self):
        global camera_pos, camera_look_at
        if self.first_person_mode:
            x, y, z = self.player_spawn_coordinate
            direction_x = math.cos(math.radians(self.player_angle - 90))
            direction_y = math.sin(math.radians(self.player_angle - 90))
            camera_pos = (x+(self.player_head_radius + 2)*direction_x, y + direction_y*(self.player_head_radius + 2), z + self.player_body_height+self.player_leg_height + (self.player_head_radius*0.8))
            offset = 100
            camera_look_at = (x + 100*direction_x, y + 100*direction_y, z + self.player_body_height+self.player_leg_height + (self.player_head_radius*0.8))

        else:
            camera_pos = (650, -650, 650)
            camera_look_at = (0,0,0)



        

    def draw_protagonist(self):
        init_x, init_y, init_z = self.player_spawn_coordinate
        glPushMatrix()
        glTranslatef(init_x, init_y, init_z)
        glRotatef(self.player_angle , 0, 0, 1)
        # body
        glPushMatrix()
        glColor3f(95/255, 127/255, 87/255)
        glTranslatef(0, 0, (1.5*self.player_leg_height))
        glScalef(1.5, 1, 2)
        glutSolidCube(self.player_body_height)
        glPopMatrix()        

        # legs
        # left leg
        glPushMatrix()
        glColor3f(94/255, 143/255, 208/255)
        glTranslatef(-10, 0, 0)
        gluCylinder(gluNewQuadric(), self.player_leg_max_radius*(2/3), self.player_leg_max_radius,self.player_leg_height, 50, 20)
        glPopMatrix()
        # right leg
        glPushMatrix()
        glColor3f(94/255, 143/255, 208/255)
        glTranslatef(10, 0, 0)
        gluCylinder(gluNewQuadric(), self.player_leg_max_radius*(2/3), self.player_leg_max_radius,self.player_leg_height, 50, 20)
        glPopMatrix()

        # head
        glPushMatrix()
        glColor3f(51/255, 51/255, 51/255)
        glTranslatef(0, 0,  self.player_body_height+self.player_leg_height + (self.player_body_height*1.2))
        gluSphere(gluNewQuadric(), self.player_head_radius, 80, 80)
        glPopMatrix()

        # hands
        # hand 1
        glPushMatrix()
        glColor3f(232/255, 195/255, 166/255)
        glTranslatef(10, -5,  self.player_body_height+self.player_leg_height )
        glRotatef(-90, 0, 1, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), self.player_leg_max_radius, self.player_leg_max_radius*(3/4),self.player_width, 50, 20)
        glPopMatrix()
        # hand 2
        glPushMatrix()
        glColor3f(232/255, 195/255, 166/255)
        glTranslatef(-10, -5,  self.player_body_height+self.player_leg_height )
        glRotatef(-90, 0, 1, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), self.player_leg_max_radius, self.player_leg_max_radius*(3/4),self.player_width, 50, 20)
        glPopMatrix()        

        # gun
        glPushMatrix()
        glColor3f(126/255, 127/255, 106/255)
        glTranslatef(0, -5, self.player_body_height+self.player_leg_height )
        glRotatef(-90, 0, 1, 0)
        glRotatef(90, 1, 0, 0)
        gluCylinder(gluNewQuadric(), self.player_leg_max_radius, self.player_leg_max_radius*(3/4),self.gun_height, 50, 20)
        self.gun_facing = [0, -5-self.gun_height, self.player_body_height+self.player_leg_height ]
        glPopMatrix()         
        glPopMatrix()       

    def enemy_jiggle(self):
        if not self.enemy_expand:
                self.enemy_radius  -= self.enemy_jiggle_speed
                if self.enemy_radius <= self.player_body_height :
                    self.enemy_radius = self.player_body_height
                    self.enemy_expand = True
        else:
            self.enemy_radius += self.enemy_jiggle_speed
            if self.enemy_radius >= self.player_body_height*1.5 :
                self.enemy_radius = self.player_body_height*1.5
                self.enemy_expand = False

    def draw_enemies(self):
        for i in self.enemies_spwan_coordinate:
            e_x, e_y, e_z = i
            glPushMatrix()
            glTranslatef(e_x, e_y, e_z)
            glColor3f(216/255, 92/255, 92/255)
            gluSphere(gluNewQuadric(), self.enemy_radius, 80 , 80)
            glPopMatrix()
            glPushMatrix()
            glTranslatef(e_x, e_y, e_z + self.enemy_radius)
            glColor3f(38/255, 38/255, 38/255)
            gluSphere(gluNewQuadric(), self.enemy_radius//2, 80, 80)
            glPopMatrix()
    
    def move_enemies(self):
        for i in range(len(self.enemies_spwan_coordinate)):
            x, y, z = self.enemies_spwan_coordinate[i]
            target_x, target_y, target_z = self.player_spawn_coordinate
            x += (target_x - x)*0.0005
            y += (target_y - y)*0.0005
            # gun_point_x, gun_point_y, gun_point_z = self.gun_facing
            person_x, person_y, person_z = self.player_spawn_coordinate
            # distance_from_gun = math.sqrt(((gun_point_x - x)**2) + (gun_point_y - y)**2)
            distance_from_person =  math.sqrt(((person_x - x)**2) + (person_y - y)**2)
            if  (distance_from_person < self.enemy_radius ) :
                self.isAlive = False
                return
            self.enemies_spwan_coordinate[i] = (x,y,z)

    def kill_and_respwan_enemies(self):
        for i in range(len(self.bullets)):
            x, y, z = self.bullets[i]["bullet_coord"]
            bullets_dir = self.bullets[i]['bullet_dir']

            for  j in range(len(self.enemies_spwan_coordinate)):
                enemy_x, enemy_y, _ = self.enemies_spwan_coordinate[j]
                distance = math.sqrt(((enemy_x - x)**2) + ((enemy_y - y)**2))
                if self.enemy_radius + self.bullet_size > distance:
                    self.bullets.pop(i)
                    self.make_bullet()                 
                    self.enemies_spwan_coordinate.pop(j)
                    self.enemy_locations()
 


                
            
            

    def bullet_movement(self):
        # if self.bullet_fired: 
            for i in self.bullets:
                bullet_coord = i["bullet_coord"]
                bullet_dir = i["bullet_dir"]
                b_x_n = bullet_coord[0] + self.bullet_speed * bullet_dir[0]
                b_y_n = bullet_coord[1] + self.bullet_speed * bullet_dir[1]
                if (-GRID_WIDTH//2 < b_x_n < GRID_WIDTH//2 and -GRID_WIDTH//2 < b_y_n < GRID_WIDTH//2) :
                    bullet_coord[0] = b_x_n; bullet_coord[1] = b_y_n    
                    i["bullet_coord"] =  bullet_coord
                else:
                    self.bullets.remove(i)

    def draw_bullet(self):
        for i in self.bullets:
            glPushMatrix()
            glColor3f(1, 0, 0)
            bullet_coord = i["bullet_coord"]
            glTranslatef(bullet_coord[0], bullet_coord[1], bullet_coord[2])
            glutSolidCube(self.bullet_size)
            glPopMatrix()
        
    def  make_bullet(self):
            p_x, p_y, p_z = self.player_spawn_coordinate
            dir_x = math.cos(math.radians(self.player_angle-90))    
            dir_y = math.sin(math.radians(self.player_angle-90))    
            bu_x = p_x + dir_x * self.gun_height
            bu_y = p_y + dir_y * self.gun_height
            bu_z = p_z + self.player_body_height + self.player_leg_height
            bullet_coord = [bu_x, bu_y, bu_z]
            bullet_dir = [dir_x, dir_y]
            self.bullets.append({
                'bullet_coord' : bullet_coord,
                'bullet_dir' : bullet_dir
            })        
        
    def MouseListener(self, key, state, x, y):
        if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            self.make_bullet()
        elif key == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            self.first_person_mode = not self.first_person_mode
 

    def KeyboardListener(self, key, x, y):
        global field_of_view
        if debug_mode:
            if key == b"w":
                field_of_view -= 1
            elif key == b"s":
                field_of_view += 1
            return 
        x, y, z = self.player_spawn_coordinate
        dir_x = math.cos(math.radians(self.player_angle-90))
        dir_y = math.sin(math.radians(self.player_angle-90))
        if key == b"w":
            a, b = x + dir_x*self.player_speed, y + dir_y*self.player_speed
            self.gun_facing[0], self.gun_facing[1] = self.gun_facing[0]+a, self.gun_facing[1] + b
            if -GRID_WIDTH//2 < self.gun_facing[0] < GRID_WIDTH//2 and  -GRID_WIDTH//2 < self.gun_facing[1] < GRID_WIDTH//2:
                x = a
                y = b
            self.player_spawn_coordinate = (x, y , z)
        elif key == b"s":
            a, b = x - dir_x*self.player_speed, y - dir_y*self.player_speed
            self.gun_facing[0], self.gun_facing[1] = self.gun_facing[0]+self.gun_height-a, self.gun_facing[1] + self.gun_height - b
            if -GRID_WIDTH//2 < self.gun_facing[0] < GRID_WIDTH//2 and  -GRID_WIDTH//2 < self.gun_facing[1] < GRID_WIDTH//2:
                x = a
                y = b
            self.player_spawn_coordinate = (x, y , z)

        elif key == b"a":
            self.player_angle += 5
        elif key == b"d":
            self.player_angle -= 5       





    def specialKeyListener(self, key, x, y):
        global camera_pos , camera_height,field_of_view
        x, y, z = camera_pos
        if key == GLUT_KEY_LEFT:
            angle_of_rotation = math.radians(1)
            x = x*math.cos(angle_of_rotation) - y*math.sin(angle_of_rotation)
            y = x*math.sin(angle_of_rotation) + y*math.cos(angle_of_rotation)
            print(x, y)
        elif key == GLUT_KEY_RIGHT:
            angle_of_rotation = math.radians(-1)
            x = x*math.cos(angle_of_rotation) - y*math.sin(angle_of_rotation)
            y = x*math.sin(angle_of_rotation) + y*math.cos(angle_of_rotation)
            print(x, y)
        elif key == GLUT_KEY_UP:
            z += 5
        elif key == GLUT_KEY_DOWN:
            z -= 5
        camera_pos = (x, y, z)
            
        
    def animation(self):
        if self.isAlive:
            glutPostRedisplay()

    def draw_walls(self, axis_close):
        floor_max_right = -GRID_WIDTH//2
        floor_max_left = GRID_WIDTH//2
        floor_max_front = GRID_LENGTH//2
        floor_max_behind = -GRID_LENGTH//2        
        length = GRID_LENGTH // 13
        width = GRID_WIDTH // 13         
        grid_wall_height = length          
        if axis_close == "+x":
            # wall on x
            glColor3f(78/255,203/255,298/255)
            # glColor3f(1, 0, 0)
            glBegin(GL_QUADS)        
            glVertex3f(floor_max_right, floor_max_front, 0)
            glVertex3f(floor_max_right, floor_max_behind, 0)
            glVertex3f(floor_max_right, floor_max_behind, grid_wall_height)
            glVertex3f(floor_max_right, floor_max_front, grid_wall_height)        
            glEnd()          
        elif axis_close == "+y" :
            # wall on y
            glColor3f(85/255,201/255,122/255)
            # glColor3f(0, 1, 1)
            glBegin(GL_QUADS)        
            glVertex3f(floor_max_left, floor_max_front, 0)
            glVertex3f(floor_max_right, floor_max_front, 0)
            glVertex3f(floor_max_right, floor_max_front, grid_wall_height)
            glVertex3f(floor_max_left, floor_max_front, grid_wall_height)
            glEnd()
        elif axis_close == "-y" :
            # wall on -y
            glColor3f(78/255,127/255,198/255)
            # glColor3f(1, 0, 1)
            glBegin(GL_QUADS)        
            glVertex3f(floor_max_left, floor_max_behind, 0)
            glVertex3f(floor_max_right, floor_max_behind, 0)
            glVertex3f(floor_max_right, floor_max_behind, grid_wall_height)
            glVertex3f(floor_max_left, floor_max_behind, grid_wall_height)       
            glEnd()     
        elif axis_close == "-x":
            # wall on -x side
            glColor3f(239/255,239/255,242/255)
            # glColor3f(1, 1, 0)
            glBegin(GL_QUADS)

            glVertex3f(floor_max_left, floor_max_front, 0)
            glVertex3f(floor_max_left, floor_max_behind, 0)
            glVertex3f(floor_max_left, floor_max_behind, grid_wall_height)
            glVertex3f(floor_max_left, floor_max_front, grid_wall_height)      
            glEnd()                    
        
        
    
    def draw_environment(self):
        # the game floor grid
        floor_max_right = -GRID_WIDTH//2
        floor_max_left = GRID_WIDTH//2
        floor_max_front = GRID_LENGTH//2
        floor_max_behind = -GRID_LENGTH//2
        l = 0
        length = GRID_LENGTH // 13
        width = GRID_WIDTH // 13        
        for i in range(floor_max_front, floor_max_behind, -GRID_WIDTH // 13  ):
            k = 0 if l % 2 == 0 else  1
            for j in range(floor_max_left, floor_max_right, -GRID_WIDTH//13  ):
                # floor grid
                glBegin(GL_QUADS)
                if k % 2 == 0:
                    glColor3f(239/255, 239/255, 242/255)
                else:
                    glColor3f(155/255, 127/255, 227/255)
                glVertex3f(j, i, 0)
                glVertex3f(j-width, i, 0)
                glVertex3f(j-width, i-length, 0)
                glVertex3f(j, i-length, 0)
                glEnd()
                k += 1
            l += 1
        x, y ,z = camera_pos
        wall_distance_from_camera = {
            "+x" : math.sqrt(((x + GRID_WIDTH//2)**2) + ((y-0)**2) + ((z-0)**2)),
            "+y" : math.sqrt(((x - 0)**2) + ((y- GRID_LENGTH//2)**2) + ((z-0)**2)),
            "-y":math.sqrt(((x - 0)**2) + ((y + GRID_LENGTH//2)**2) + ((z-0)**2)),
            "-x":math.sqrt(((x - GRID_WIDTH//2)**2) + ((y-0)**2) + ((z-0)**2)),            
        }
        wall_distance_from_camera = dict(sorted(wall_distance_from_camera.items(),key = lambda item:item[1],  reverse=True))
        for  key, value in wall_distance_from_camera.items():
            self.draw_walls(key)




    def setupCamera(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(field_of_view, window_width/window_height, 0.1, 1500)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        x, y, z = camera_pos
        look_x, look_y,look_z = camera_look_at
        respect_to_x, respect_to_y, respect_to_z = axis_decision
        gluLookAt(x, y, z,
                  look_x, look_y,look_z,
                  respect_to_x, respect_to_y, respect_to_z)

    def showScreen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glViewport(0, 0, window_width, window_height)
        self.reset_camera()
        self.setupCamera()        
        self.draw_environment()
        self.draw_protagonist()
        self.bullet_movement()
        self.draw_bullet()
        self.draw_enemies()
        self.enemy_jiggle()
        self.move_enemies()
        self.kill_and_respwan_enemies()
        glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(0,0)
    window = glutCreateWindow(b"Assignment 3")
    glEnable(GL_DEPTH_TEST)
    game = Game()
    glutDisplayFunc(game.showScreen)
    glutKeyboardFunc(game.KeyboardListener)
    glutSpecialFunc(game.specialKeyListener)
    glutMouseFunc(game.MouseListener)
    glutIdleFunc(game.animation)
    glutMainLoop()

if __name__ == "__main__":
    main()



                        

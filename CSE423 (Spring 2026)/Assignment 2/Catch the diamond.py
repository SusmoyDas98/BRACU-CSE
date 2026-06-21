from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time
import math
window_width, window_height = 450, 600
game = None
frame_time = None
time_passed = None

class Mid_Point_Line_Drawing:
    
    def __init__(self, x1, y1, x2, y2, colors):
        self.x1, self.y1, self.x2, self.y2  = x1, y1, x2, y2
        self.colors = colors
        self.zone = self.find_zone(self.x1, self.y1, self.x2, self.y2)

    def find_zone(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1 
        Zone = 0
        if dx >= 0 and dy >= 0:
            Zone = 1 if abs(dx) < abs(dy) else 0
        elif dx < 0 and dy >= 0:
            Zone = 3 if abs(dx) >= abs(dy) else 2
        elif dx < 0 and dy < 0:
            Zone = 4 if abs(dx) >= abs(dy) else 5
        elif dx >= 0 and dy < 0:
            Zone = 7 if abs(dx) >= abs(dy) else 6
        return Zone
  
    def shift_zone(self, x1, y1, from_zone, to_zone = 0):
        coordinates = [x1, y1]
        if from_zone == to_zone : return coordinates
        if from_zone != 0 and to_zone == 0:
            if from_zone == 1:
                coordinates[0], coordinates[1] = coordinates[1], coordinates[0]
            elif from_zone == 2:
                coordinates[0], coordinates[1] = coordinates[1], (-1) * coordinates[0]
            elif from_zone == 3:
                coordinates[0], coordinates[1] = (-1) * coordinates[0], coordinates[1]
            elif from_zone == 4:
                coordinates[0], coordinates[1] = (-1) * coordinates[0], (-1) * coordinates[1]
            elif from_zone == 5:
                coordinates[0], coordinates[1] = (-1) * coordinates[1], (-1) * coordinates[0]
            elif from_zone == 6:
                coordinates[0], coordinates[1] = (-1) * coordinates[1], coordinates[0]         
            elif from_zone == 7:
                coordinates[0], coordinates[1] = coordinates[0], (-1) * coordinates[1]

        elif from_zone == 0 and to_zone != 0:
            if to_zone == 1:
                coordinates[0], coordinates[1] = coordinates[1], coordinates[0]
            elif to_zone == 2:
                coordinates[0], coordinates[1] = (-1) * coordinates[1], coordinates[0]
            elif to_zone == 3:
                coordinates[0], coordinates[1] = (-1) * coordinates[0], coordinates[1]
            elif to_zone == 4:
                coordinates[0], coordinates[1] = (-1) * coordinates[0], (-1) * coordinates[1]
            elif to_zone == 5:
                coordinates[0], coordinates[1] = (-1) * coordinates[1], (-1) * coordinates[0]
            elif to_zone == 6:
                coordinates[0], coordinates[1] =  coordinates[1], (-1) * coordinates[0]         
            elif to_zone == 7:
                coordinates[0], coordinates[1] = coordinates[0], (-1) * coordinates[1]            

        return coordinates

    def Draw_Line(self,x, y):
        x_og, y_og = self.shift_zone(x, y, 0, self.zone) if self.zone != 0 else [x,y]
        glPointSize(2)
        r, g, b = self.colors
        glColor3f(r, g, b)
        glBegin(GL_POINTS)
        glVertex2d(x_og,y_og)
        glEnd()

    def MNP_algo(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        d = 2*(dy) - dx
        inc_East = 2*dy
        inc_NorthEast = 2*dy - 2*dx
        y = y1
        for x in range(x1, x2+1):
            self.Draw_Line(x,y)
            if d>0:
                d += inc_NorthEast
                y += 1
            else:
                d += inc_East
 
    def render_points(self):
        given_zone = self.zone
        if given_zone > 0:
            starting_coordinate,  ending_coordinate = self.shift_zone(self.x1, self.y1, given_zone), self.shift_zone(self.x2, self.y2, given_zone) 
        else:
            starting_coordinate,  ending_coordinate = [self.x1, self.y1], [self.x2, self.y2]
        if starting_coordinate[0] > ending_coordinate[0] :
            starting_coordinate, ending_coordinate = ending_coordinate, starting_coordinate
        self.MNP_algo(starting_coordinate[0], starting_coordinate[1], ending_coordinate[0], ending_coordinate[1])




class Catch_The_Diamonds:

    def __init__(self):
        self.catcher_speed = 900
        self.speed_increase_rate_catcher = 35
        self.diamond_speed = 120
        self.speed_increase_rate_diamond = 8
        self.catcher_color = (1,1,1)
        self.move_right = False
        self.move_left = False        
        self.is_missed = False
        self.total_points = 0
        self.is_paused = False
        self.catcher_bottom_start, self.catcher_bottom_end = [30, 0], [110, 0]
        self.catcher_center_bottom_start, self.catcher_center_bottom_end = [window_width//2 - 40, 0], [window_width//2 + 40, 0]
        self.catcher_top_start, self.catcher_top_end = [10, 30], [130, 30]
        self.catcher_center_top_start, self.catcher_center_top_end = [window_width//2 - 60, 30], [window_width//2 + 60, 30]
        self.reload_button_position = [20, window_height-35]
        self.reload_button_color = (0, 1, 1)
        self.pause_play_button_position_from_center = [window_width//2, window_height-35]
        self.pause_play_button_color = (1, 0.7, 0)
        self.pause_button_bar_gap = 20
        self.terminate_button_position_from_center = [window_width - 50, window_height-35]
        self.terminate_button_color = (1, 0, 0)
        self.button_max_width = 50
        self.button_max_height_from_center = 20
        self.diamond_width = 20
        self.diamond_height = 40
        self.diamond_position_top = [random.randint(0 + self.diamond_width, window_width - self.diamond_width), window_height - 80]
        self.diamond_color = (random.uniform(0.5,1), random.uniform(0.5,1), random.uniform(0.5,1))
        self.cheat_activated = False
         
    @staticmethod
    def draw_line(x1, y1, x2, y2, color):
        line = Mid_Point_Line_Drawing( x1, y1, x2, y2, color)
        line.render_points()

    def draw_catcher(self):
        # catcher bottom
        x_start_bottom, y_start_bottom = self.catcher_bottom_start
        x_end_bottom, y_end_bottom = self.catcher_bottom_end
        self.draw_line(x_start_bottom, y_start_bottom, x_end_bottom, y_end_bottom, self.catcher_color)

        # catcher top
        x_start_top, y_start_top = self.catcher_top_start
        x_end_top, y_end_top = self.catcher_top_end
        self.draw_line(x_start_top, y_start_top, x_end_top, y_end_top, self.catcher_color)        

        # catcher left corner
        x_left_bottom, y_left_bottom = self.catcher_bottom_start
        x_left_top, y_left_start = self.catcher_top_start
        self.draw_line(x_left_bottom, y_left_bottom ,  x_left_top, y_left_start, self.catcher_color)            

        # catcher right corner
        x_right_bottom, y_right_bottom = self.catcher_bottom_end
        x_right_top, y_right_start = self.catcher_top_end
        self.draw_line(x_right_bottom, y_right_bottom ,x_right_top, y_right_start, self.catcher_color)        

        # self.catcher_top_area = [(x_start_top, y_start_top), (x_end_top, y_end_top)]
        self.catcher_area = (
            (x_start_top, x_end_top),
            (y_start_top, y_end_bottom)  
        )

    def animate_catcher(self, time_passed):
        if self.is_paused : return
        if self.cheat_activated:            
            self.catcher_center = (self.catcher_top_start[0] + self.catcher_top_end[0]) // 2
            move = int(self.catcher_speed * time_passed) 
            if self.diamond_position_top[0] > self.catcher_center:
                distance = self.diamond_position_top[0] - self.catcher_center
                available_move = window_width - 10 - self.catcher_top_end[0]
                allowed_move = min(available_move, distance)
                final_move_right = min(allowed_move, move)
                if final_move_right > 0:
                    self.catcher_bottom_start[0] += final_move_right
                    self.catcher_bottom_end[0] += final_move_right
                    self.catcher_top_start[0] += final_move_right
                    self.catcher_top_end[0] +=      final_move_right  

            elif   self.diamond_position_top[0] < self.catcher_center:
                distance = self.catcher_center - self.diamond_position_top[0]
                available_move = self.catcher_top_start[0]   -  10 
                allowed_move = min(available_move, distance)
                final_move_left = min(allowed_move, move)
                if final_move_left > 0:
                    self.catcher_bottom_start[0] -= final_move_left
                    self.catcher_bottom_end[0] -= final_move_left
                    self.catcher_top_start[0] -= final_move_left
                    self.catcher_top_end[0] -= final_move_left  
        else:           
            if self.move_right:
                self.catcher_bottom_start[0] += int(self.catcher_speed * time_passed)
                self.catcher_bottom_end[0] += int(self.catcher_speed * time_passed)
                self.catcher_top_start[0] += int(self.catcher_speed * time_passed)
                self.catcher_top_end[0] += int(self.catcher_speed * time_passed)
                self.move_right =  False
            elif self.move_left:
                self.catcher_bottom_start[0] -= int(self.catcher_speed * time_passed)
                self.catcher_bottom_end[0] -= int(self.catcher_speed * time_passed)
                self.catcher_top_start[0] -= int(self.catcher_speed * time_passed)
                self.catcher_top_end[0] -= int(self.catcher_speed * time_passed)
                self.move_left = False
        glutPostRedisplay()

    def is_caught(self):
        catcher_left = self.catcher_area[0][0]
        catcher_right = self.catcher_area[0][1]
        catcher_top = self.catcher_area[1][0]
        diamond_left = self.diamond_area[0][0]
        diamond_right = self.diamond_area[0][1]
        diamond_bottom = self.diamond_area[1][1]
        diamond_center = (diamond_left + diamond_right)//2
        if ( catcher_left <=  diamond_center <= catcher_right or  catcher_left <=  diamond_center+self.diamond_width//2 <= catcher_right or  catcher_left <=  diamond_center - self.diamond_width//2 <= catcher_right  ) and diamond_bottom <= catcher_top:
            return True
        else:
            return False

    def animate_diamond(self, time_passed):
        if self.is_paused: return 
        self.diamond_position_top[1] = (self.diamond_position_top[1] - math.ceil(self.diamond_speed * time_passed))
        if self.is_caught() :
            self.total_points += 1
            # speed increment 
            self.diamond_speed += self.speed_increase_rate_diamond
            self.catcher_speed += self.speed_increase_rate_catcher
            print(f"Score: {self.total_points}")
            self.diamond_position_top = [random.randint(0 + self.diamond_width, window_width - self.diamond_width), window_height - 80]
            self.diamond_color = (random.uniform(0.5,1), random.uniform(0.5,1), random.uniform(0.5,1))
        
        elif self.diamond_position_top[1] < 0 :
            self.is_paused = True 
            self.is_missed = True
            self.catcher_color = (1, 0, 0)        
            print("Game Over! Score:", self.total_points)
    
    def catcher_direction(self, key, x, y):
        if key == GLUT_KEY_RIGHT and self.catcher_top_end[0] + int(self.catcher_speed * time_passed) < window_width - 10:
            self.move_right = True
            self.move_left = False
        elif key == GLUT_KEY_LEFT and self.catcher_top_start[0] - int(self.catcher_speed * time_passed) > 10:       
            self.move_left = True
            self.move_right = False
        glutPostRedisplay()

    def draw_buttons(self):
        # reload button - body
        reload_x_start, reload_y_start = self.reload_button_position
        reload_x_end, reload_y_end = [self.reload_button_position[0] + self.button_max_width, self.reload_button_position[1]]
        self.draw_line(
            reload_x_start,
            reload_y_start, 
            reload_x_end, 
            reload_y_end, 
            self.reload_button_color
            )
        # reload button arrow-head 
        reload_arrow_range = 20       
        reload_arrow_start_x, reload_arrow_start_y = self.reload_button_position
        reload_arrow_top_end_x, reload_arrow_top_end_y =  [self.reload_button_position[0] + reload_arrow_range, self.reload_button_position[1] + self.button_max_height_from_center]
        self.draw_line(
            reload_arrow_start_x, 
            reload_arrow_start_y, 
            reload_arrow_top_end_x, 
            reload_arrow_top_end_y, 
            self.reload_button_color
            )
        reload_arrow_bottom_end_x, reload_arrow_bottom_end_y =  [self.reload_button_position[0] + reload_arrow_range, self.reload_button_position[1] - self.button_max_height_from_center]
        self.draw_line(
            reload_arrow_start_x, 
            reload_arrow_start_y, 
            reload_arrow_bottom_end_x, 
            reload_arrow_bottom_end_y, 
            self.reload_button_color 
            )
        
        '''
        area tuple = (
        (left, right), (top, bottom)
        )
        '''

        self.reload_button_area = (
            (reload_x_start, reload_x_end), 
            (reload_arrow_top_end_y, reload_arrow_bottom_end_y)
        )
        
        # pause button
        if not self.is_paused:
            pause_button_center_x, pause_button_center_y = self.pause_play_button_position_from_center
            # pause button left bar
            pause_button_left_bar_center_x, pause_button_left_bar_center_y = pause_button_center_x - self.button_max_width//5, pause_button_center_y
            self.draw_line(
                pause_button_left_bar_center_x, 
                pause_button_left_bar_center_y + self.button_max_height_from_center, 
                pause_button_left_bar_center_x, 
                pause_button_left_bar_center_y - self.button_max_height_from_center, 
                self.pause_play_button_color
                )
    
            # pause button right bar
            pause_button_right_bar_center_x, pause_button_right_bar_center_y = pause_button_center_x + self.button_max_width//5, pause_button_center_y
            self.draw_line(
                pause_button_right_bar_center_x, 
                pause_button_right_bar_center_y + self.button_max_height_from_center, 
                pause_button_right_bar_center_x, 
                pause_button_right_bar_center_y - self.button_max_height_from_center, 
                self.pause_play_button_color
                )

            self.pause_button_area = (
                (pause_button_left_bar_center_x, pause_button_right_bar_center_x),
                (pause_button_left_bar_center_y + self.button_max_height_from_center, pause_button_left_bar_center_y - self.button_max_height_from_center)
            )

        else:
            # play button
            play_button_center_x, play_button_center_y = self.pause_play_button_position_from_center

            # play button pointy head
            play_button_pointer_x, play_button_pointer_y = play_button_center_x + self.button_max_width//2, play_button_center_y
            # play button flat side
            play_button_flat_end_center_x, play_button_flat_end_center_y =  play_button_center_x - self.button_max_width//2, play_button_center_y
            self.draw_line(
                play_button_pointer_x, 
                play_button_pointer_y,
                play_button_flat_end_center_x, 
                play_button_flat_end_center_y + self.button_max_height_from_center, 
                self.pause_play_button_color 
                )
            self.draw_line(
                play_button_pointer_x, 
                play_button_pointer_y,
                play_button_flat_end_center_x, 
                play_button_flat_end_center_y - self.button_max_height_from_center, 
                self.pause_play_button_color 
                )            
            self.draw_line(
                play_button_flat_end_center_x, 
                play_button_flat_end_center_y + self.button_max_height_from_center, 
                play_button_flat_end_center_x, 
                play_button_flat_end_center_y - self.button_max_height_from_center, 
                self.pause_play_button_color
                )
            self.play_button_area = (
                (play_button_flat_end_center_x, play_button_pointer_x),
                (play_button_pointer_y + self.button_max_height_from_center, play_button_pointer_y - self.button_max_height_from_center )
            )

        # terminate button
        terminate_button_center_x, terminate_button_center_y = self.terminate_button_position_from_center
        self.draw_line(
            terminate_button_center_x - self.button_max_width//2, 
            terminate_button_center_y + self.button_max_height_from_center,
            terminate_button_center_x + self.button_max_width//2, 
            terminate_button_center_y - self.button_max_height_from_center,
            self.terminate_button_color
            )
        self.draw_line(
            terminate_button_center_x + self.button_max_width//2, 
            terminate_button_center_y + self.button_max_height_from_center,
            terminate_button_center_x - self.button_max_width//2, 
            terminate_button_center_y - self.button_max_height_from_center,
            self.terminate_button_color
            )        
        self.terminate_button_area = (
            (terminate_button_center_x - self.button_max_width//2, terminate_button_center_x + self.button_max_width//2),
            (terminate_button_center_y + self.button_max_height_from_center, terminate_button_center_y - self.button_max_height_from_center)
        )

    def cheat_mode(self, key, x, y ):
        if key == b"c" and self.is_missed == False and not self.is_paused:
            if self.cheat_activated == False:
                self.cheat_activated = True
                print("Cheat Mode Activated")
            elif self.cheat_activated == True:
                self.cheat_activated = False
                print('Cheat Mode Deactivated')

    def button_listeners(self, key, state, x, y):
        if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            # play button
            if self.is_paused:
                x_min_play = self.play_button_area[0][0]
                x_max_play = self.play_button_area[0][1]
                y_top_play = self.play_button_area[1][0]
                y_bottom_play = self.play_button_area[1][1]    
            # pause button
            if not self.is_paused:
                x_min_pause = self.pause_button_area[0][0]
                x_max_pause = self.pause_button_area[0][1]
                y_top_pause = self.pause_button_area[1][0]
                y_bottom_pause = self.pause_button_area[1][1]       
            # terminate button 
            x_min_terminate = self.terminate_button_area[0][0]
            x_max_terminate = self.terminate_button_area[0][1]
            y_top_terminate = self.terminate_button_area[1][0]
            y_bottom_terminate = self.terminate_button_area[1][1]    
            # reload button
            x_min_reload = self.reload_button_area[0][0]
            x_max_reload = self.reload_button_area[0][1]
            y_top_reload = self.reload_button_area[1][0]
            y_bottom_reload = self.reload_button_area[1][1]                
                                            
            # play button
            if self.is_paused and (x_min_play <= x <= x_max_play and y_bottom_play <= window_height - y <= y_top_play):
                    if not self.is_missed:
                        self.is_paused = False
            elif not self.is_paused and (x_min_pause <= x <= x_max_pause and y_bottom_pause <= window_height - y <= y_top_pause):
                    self.is_paused = True
            elif (x_min_terminate <= x <= x_max_terminate and y_bottom_terminate <= window_height - y <= y_top_terminate):
                print(f"Goodbye! Score: {self.total_points}")
                glutLeaveMainLoop()
            
            # reload button
            elif (x_min_reload <= x <= x_max_reload and y_bottom_reload <= window_height - y <= y_top_reload):
                if self.is_paused :
                    self.is_paused = False
                    self.catcher_color = (1,1,1)
                    self.catcher_speed = 900
                    self.diamond_speed = 120
                self.diamond_position_top = [random.randint(0 + self.diamond_width, window_width - self.diamond_width), window_height - 
                80]                    
                self.diamond_color = (random.uniform(0.5,1), random.uniform(0.5,1), random.uniform(0.5,1))
                self.catcher_top_start, self.catcher_top_end = self.catcher_center_top_start.copy(), self.catcher_center_top_end.copy()
                self.catcher_bottom_start, self.catcher_bottom_end = self.catcher_center_bottom_start.copy(), self.catcher_center_bottom_end.copy() 
                self.total_points = 0
                self.is_missed = False
                self.cheat_activated = False
                self.catcher_bottom_start 
                print("Starting Over")                
        glutPostRedisplay()


    def draw_diamonds(self):
        diamond_top_x, diamond_top_y = self.diamond_position_top
        self.draw_line(
            diamond_top_x, 
            diamond_top_y, 
            diamond_top_x - self.diamond_width//2,
            diamond_top_y - self.diamond_height//2,
            self.diamond_color
            )
        self.draw_line(
            diamond_top_x, 
            diamond_top_y, 
            diamond_top_x + self.diamond_width//2,
            diamond_top_y - self.diamond_height//2,
            self.diamond_color
            )        
        self.draw_line(
            diamond_top_x, 
            diamond_top_y - self.diamond_height, 
            diamond_top_x - self.diamond_width//2,
            diamond_top_y - self.diamond_height//2,
            self.diamond_color
            )        
        self.draw_line(
            diamond_top_x, 
            diamond_top_y - self.diamond_height, 
            diamond_top_x + self.diamond_width//2,
            diamond_top_y - self.diamond_height//2,
            self.diamond_color
            )              
        self.diamond_area = (
            (diamond_top_x - self.diamond_width//2, diamond_top_x + self.diamond_width//2),
            (diamond_top_y , diamond_top_y - self.diamond_height)
        )

    def render_game_visuals(self):
        catcher_path_x_max = window_width
        catcher_path_y_max = window_height
        self.draw_catcher()
        self.draw_buttons()
        if  self.is_missed == False:
            self.draw_diamonds()



def animations():
    global frame_time, time_passed
    current_time = time.time()
    time_passed = current_time - frame_time
    frame_time = current_time
    game.animate_catcher(time_passed)
    game.animate_diamond(time_passed)
    
def projections():
    glViewport(0, 0, window_width, window_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0 ,window_width, 0, window_height, 0, 1)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    game.render_game_visuals()
    glutSwapBuffers()

def main():
    global frame_time
    frame_time = time.time()
    global game
    game = Catch_The_Diamonds()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(window_width, window_height)
    glutInitWindowPosition(700,10)
    glutCreateWindow(b"Catch the Diamonds")
    projections()
    glutDisplayFunc(display)
    glutIdleFunc(animations)
    glutSpecialFunc(game.catcher_direction)
    glutMouseFunc(game.button_listeners)
    glutKeyboardFunc(game.cheat_mode)
    glutMainLoop()

if __name__ == "__main__":
    main()

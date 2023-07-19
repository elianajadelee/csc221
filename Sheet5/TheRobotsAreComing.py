from gasp import *
from random import randint


def place_player():
    global player_x, player_y, player_shape

    player_x = randint(0, 63)
    player_y = randint(0, 47)
    player_shape = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled=True)


def place_robot():
    global robot_shape, robot_x, robot_y
    
    robot_x = randint(0, 63)
    robot_y = randint(0, 47)
    robot_shape = Circle((10 * robot_x + 5 , 10 * robot_y + 5), 5)


def move_player():
    global player_x, player_y, player_shape, finished
    
    key = update_when('key_pressed')
   
    if key == 'Right':
        player_x += 1
    if key == 'Left':
        player_x -= 1
    if key == 'Up':
        player_y += 1
    if key == 'Down': 
        player_y -= 1
    if key == 'q':
        finished = True
        
    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))


def move_robot():
    global robot_shape, robot_x, robot_y, player_x, player_y
    print('robot move')
    if robot_y > player_y:
        robot_y -= 1
    if robot_y < player_y:
        robot_y +=1
    if robot_x > player_x:
        robot_x -= 1
    if robot_x < player_x:
        robot_x += 1

    move_to(robot_shape, (10 * robot_x, 10 * robot_y))

def check_collisions():
    global finished 
    
    if player_x == robot_x and player_y == robot_y:
        Text("GAME OVER!", (50, 50), size=50)
    finished = True

begin_graphics()
finished = False 
player = place_player()
robot = place_robot()

while not finished:
    move_player()
    move_robot()
while finished:
    check_collisions()
end_graphics()

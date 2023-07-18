from gasp import*

begin_graphics()
finished = False 

from random import randint
player_x = randint(0,63)
player_y = randint(0,47)
robot_x = randint(0, 63)
robot_y = randint(0, 47)

c = Circle((10 * robot_x +5 , 10 * robot_y + 5), 5)
move_to(c, (300, 220))

def move_player():
    print("I'm moving...")

def place_player():
    global c
    c = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True)

def move_robot():
    global robot_x, robot_y, b
    print('robot move')
    if robot_y > player_y:
        robot_y -= 1
    if robot_y < player_y:
        robot_y +=1
    if robot_x > player_x:
        robot_x -= 1
    if robot_x < player_x:
        robot_x += 1
        move_to(c, (10 * robot_x, 10 * robot_y))

while True: 
   
    player = Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    
    key = update_when('key_pressed')
   
    remove_from_screen(player)
    
    if key == 'Right':
        player_x += 1
    if key == 'Left':
        player_x -= 1
    if key == 'Up':
        player_y += 1
    if key == 'Down': 
        player_y -= 1
    if key == 'q':
        break

move_to(Circle, (10 * player_x + 5, 10 * player_y + 5))

place_player()
while not finished:
    move_player()
    move_robot()
update_when('key_pressed')
end_graphics()


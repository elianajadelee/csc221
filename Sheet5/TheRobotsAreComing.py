from gasp import*

begin_graphics()
finished = False 

def place_player():
    print("Here I am!")

def move_player():
    print("I'm moving...")

from random import randint
player_x = randint(0,63)
player_y = randint(0,47)

Circle((10* player_x + 5, 10* player_y + 5), 5, filled = True)

while not finished:
    move_player
    
update_when('key_pressed')
end_graphics()

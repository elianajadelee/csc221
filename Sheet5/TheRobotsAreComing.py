from gasp import*

begin_graphics()
finished = False 

c = Circle((320, 200), 5)
move_to(c, (300, 220))

def place_player():
    print("Here I am!")

def move_player():
    print("I'm moving...")

from random import randint
player_x = randint(0,63)
player_y = randint(0,47)

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

update_when('key_pressed')
end_graphics()

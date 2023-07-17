from gasp import*

begin_graphics()
finished = False 

def place_player():
    print("Here I am!")

def move_player():
    print("I'm moving...")

while not finished:
    move_player
    
update_when('key_pressed')
end_graphics()

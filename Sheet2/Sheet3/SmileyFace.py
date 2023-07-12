from gasp import*

begin_graphics()

Circle((100,200), 50)

Circle((85, 185), 2)

Arc((70, 210), 20, 220, 310)

Arc((100, 210), 20, 225, 315)

Arc((100, 200), 30, 225, 315)

for x in range(75,100,5):
    Arc((x, 225), 30, -225,-315)


Arc((50,200), 10, 90, 270)
Arc((150,200), 10, -90, 100)

update_when('key_pressed')
end_graphics()

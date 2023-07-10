from gasp import*

begin_graphics()

Circle((100,200),50)

Circle((85, 210), 5)

Circle((115, 210), 5)

Line((100,210), (90, 190))

Line((90,190), (110, 190))

Arc((100, 200), 30, 225, 315)

update_when('key_pressed')
end_graphics()

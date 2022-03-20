
# Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def race():
    turn_left()
    move()
    while wall_on_right():
        move()
    if right_is_clear:
        turn_right()
        move()
        turn_right()
        move()
    while front_is_clear():
        move()
    turn_left()
        
while at_goal() != True:
    if front_is_clear():
        move()
    if wall_in_front():
        race()


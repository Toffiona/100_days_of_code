def jump():
    turn_left()
    while wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    if front_is_clear() and right_is_clear():
        turn_right()
        move()
        turn_right()
        move()
        
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
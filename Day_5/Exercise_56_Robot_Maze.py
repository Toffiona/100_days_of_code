def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
 
while not at_goal():
    
    if right_is_clear():
         turn_right()
         move()
         if is_facing_north() and front_is_clear() and right_is_clear():
            move()           
         if is_facing_north() and right_is_clear():
            turn_right()
            move()
            if front_is_clear():
                move()
            
       
    elif front_is_clear():
         move() 
            
    else:
        turn_left()

Solution:
 
while front_is_clear():
    move()
turn_left()

while not at_goal():
    
    if right_is_clear():
         turn_right()
         move()
                    
       
    elif front_is_clear():
         move() 
            
    else:
        turn_left()

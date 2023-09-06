'''
Visit the link:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
'''

def turn_right():
    turn_left()
    turn_left()
    turn_left() 

while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    elif wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    elif right_is_clear:
        turn_right()
        if front_is_clear():
            move()
        else:
            turn_right()
            

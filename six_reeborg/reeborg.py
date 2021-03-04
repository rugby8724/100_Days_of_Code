def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    right = 0
    while right < 7:
        if right_is_clear():
            turn_right()
            move()
            right += 1
        else:
           break
    if front_is_clear():
       right = 0
       move()
    else:
       right = 0
       turn_left()

#website
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

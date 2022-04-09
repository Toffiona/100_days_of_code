from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")

# ADD shape (being the US MAP) to screen
image = "./Day_25/us-states-game/blank_states_img.gif"
screen.addshape(image)
# SET TURTLE WITH NEW IMAGE being the US MAP
turtle = Turtle()
turtle.shape(image)

# # CHECK X & Y coordinate of turtle on screen
# def get_mouse_click_coor(x,y):
#     print(x,y)

# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
score = 0
answer_state = screen.textinput(title="Guess a state", prompt="What's another state name?").title()

data = pandas.read_csv("./Day_25/us-states-game/50_states.csv")

# alaska = data[data.state == "Alaska"]
# print(alaska.x)
state_list = data["state"].to_list()
# print(state_list)

score = 0
guess_state =[]
while score < 50:
    for state in state_list:
        if answer_state == state:
            guess_state.append(answer_state)
            x_cor = float(data[data.state == answer_state].x)
            y_cor = float(data[data.state == answer_state].y)
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_turtle.goto(x_cor, y_cor)
            new_turtle.pendown()
            new_turtle.write(f"{answer_state}",align="center", font=("arial",10,"normal"))
            score += 1    

    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        not_guess_state_dict = {"State":[], "x":[], "y":[]}
        for state in state_list:
            if state not in guess_state:
                not_guess_state_dict["State"].append(state)
                x = int(data[data.state == state].x)
                y = int(data[data.state == state].y)
                not_guess_state_dict["x"].append(x)
                not_guess_state_dict["y"].append(y)

        #not_guess_state_dict["State"] = [state for state in state_list if state not in guess_state]
        

        states_to_learn = pandas.DataFrame(not_guess_state_dict)
        print(states_to_learn)

        states_to_learn.to_csv("./Day_25/us-states-game/states_to_learn.csv")
        break

screen.mainloop()








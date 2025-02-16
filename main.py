import pandas
import turtle
from turtle import Turtle
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
game_status = True
data = pandas.read_csv("50_states.csv")
duplicates = []

#GET THE INPUT FROM THE USER

while game_status:
    answer_state = turtle.textinput(f"{score}/50 states guessed", "What's another state name?").title()
    guessed = data[data["state"] == answer_state]
    if score <= 50:
        if not guessed.empty:
            if answer_state not in duplicates:
                guessed_x = guessed.x.item()
                guessed_y = guessed.y.item()
                text_turtle = Turtle()
                text_turtle.hideturtle()
                text_turtle.penup()
                text_turtle.goto(guessed_x, guessed_y)
                text_turtle.write(answer_state)
                score += 1
                duplicates.append(answer_state)
            else:
                pass

        else:
            print("False")
    else:
        game_status = False
















screen.exitonclick()
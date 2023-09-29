from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=(-100 + (i * 35)))
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward((random_distance))

        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

screen.exitonclick()

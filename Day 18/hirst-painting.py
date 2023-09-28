# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen, colormode
import random

colormode(255)
color_list = [(204, 154, 104), (125, 54, 59), (226, 234, 232), (120, 90, 61), (216, 208, 135), (82, 118, 154), (137, 164, 189), (46, 55, 70), (187, 156, 166), (39, 36, 32), (42, 53, 45), (96, 46, 50)]
screen = Screen()

def random_color():
    return random.choice(color_list)

coordinates = [-10,-10,190,190]
screen.setworldcoordinates(coordinates[0], coordinates[1], coordinates[2], coordinates[3])

tim = Turtle()
tim.speed("fastest")

for i in range(10):
    for _ in range(10):
        tim.dot(20,random_color())
        tim.penup()
        tim.forward((20))
    tim.home()
    tim.left(90)
    tim.forward(20 * (i+1))
    tim.right(90)

tim.hideturtle()
screen.exitonclick()

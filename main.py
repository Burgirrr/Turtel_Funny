import turtle
import random
import time

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Race")

# Create turtles for race
colors = ["red", "green", "blue", "black", "purple"]
turtles = []

start_x = -200
start_y = -100
for color in colors:
    t = turtle.Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(start_x, start_y)
    turtles.append(t)
    start_y += 50

while True:
    for turtle in turtles:
    turtle.forward(random.randint(1,10))
    screen.mainloop()
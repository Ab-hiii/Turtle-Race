import turtle
import random
from turtle import Turtle, Screen
screen = Screen()
screen.setworldcoordinates(-380, -320, 325, 320)

colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
turtles = []
y_cor = 90
for i in range(0,7):
    t = Turtle()
    t.penup()
    t.shape("turtle")
    t.color(colors[i])
    t.goto(-370, y_cor)
    y_cor-= 30
    turtles.append(t)

race_finished = False
bet = screen.textinput("Bet", "Place your bet:")
while not race_finished:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 320:
            race_finished = True
            winner = (turtle.color()[0])
            print(winner)
            break


if bet.lower() == winner.lower():
    print(f"{winner} is the winner! You win.")
else:
    print(f"{winner} was the  winner. You lose.")


screen.exitonclick()

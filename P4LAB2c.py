#CTI-110
#P4lab2 Snowflake
#Joseph Quigley
#03/10/2022
#Using Turtle and for loop to draw snoflake

import turtle

lily = turtle.Turtle()
turtle.Screen().bgcolor("lightblue")
colours = ["cyan", "purple", "blue"]
lily.color("blue")
lily.speed(10)
for i in range(10):
    for i in range(2):
        lily.forward(200)
        lily.right(60)
        lily.forward(200)
        lily.right(120)
    lily.right(36)
   

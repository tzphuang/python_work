import turtle
import math

# calls turtle package, calls the function screen, assign it to sc1
sc1 = turtle.Screen()

# create an object called turtle1
# call the package turtle that was imported
# use the function Turtle() to create a new turtle
# assign that new turtle to turtle1
turtle1 = turtle.Turtle()

turtle1.speed(0)

# draws a circle with 200 pixel radius
turtle1.circle(125)

turtle1.penup()
turtle1.goto(40,150)
turtle1.pendown()
turtle1.circle(20)

turtle1.penup()
turtle1.goto(-40,150)
turtle1.pendown()
turtle1.circle(20)

turtle1.penup()
turtle1.goto(0,150)
turtle1.pendown()
turtle1.right(90)
turtle1.forward(75)

turtle1.penup()
turtle1.goto(-50,45)
turtle1.pendown()
turtle1.right(-90)
turtle1.forward(100)

# exits the sc1 object when clicked
sc1.exitonclick()
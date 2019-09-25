import turtle
import math

# calls turtle package, calls the function screen, assign it to sc1
sc1 = turtle.Screen()

# create an object called turtle1
# call the package turtle that was imported
# use the function Turtle() to create a new turtle
# assign that new turtle to turtle1
turtle1 = turtle.Turtle()

# draws a circle with 200 pixel radius
turtle1.circle(200)

# draws a line from the point at which the circle above ends
turtle.forward(200)

# exits the sc1 object when clicked
sc1.exitonclick()
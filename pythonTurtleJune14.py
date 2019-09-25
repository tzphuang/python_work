import turtle

sc1 = turtle.Screen()

def draw_Spiral(step, iterations):
    """Draws a spiral in python"""
    turtle_Car = turtle.Turtle()
    turtle_Car.speed(10)
    for n in range(1,iterations):
        turtle_Car.forward(step)
        turtle_Car.left(360/n)

    sc1.exitonclick()

draw_Spiral(2,1000)

import turtle

screen1 = turtle.Screen()
t = turtle.Turtle()

def part_of_circle(turtle,angle, radius, color):
    """Creates a piece of pie of a circle"""
    
    turtle.color("black",color)
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius,angle)
    turtle.left(90)
    turtle.forward(radius)
    turtle.end_fill()

    t.left(180)

    #screen1.exitonclick()

#part_of_circle(t,90,200,"cyan")


def draw_pie_chart():
    """Creates a whole pie chart"""
    part_of_circle(t,120,200,"red")
    part_of_circle(t,120,200,"white")
    part_of_circle(t,120,200,"blue")
    screen1.exitonclick()

draw_pie_chart()

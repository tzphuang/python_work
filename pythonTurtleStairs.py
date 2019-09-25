# ~~python stairs in turtle~~

def make_stairs(num_steps, length, height):
    """ Draws stairs with length, heigh input, and repeated n amount of steps """
    import turtle
    sc1 = turtle.Screen()
    turtle1 = turtle.Turtle()
    for num in range(num_steps):
        turtle.left(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(length)
    sc1.exitonclick()

def main():
    make_stairs(5,20,20)



if __name__ == "__main__":
    main()
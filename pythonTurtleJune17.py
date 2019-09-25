def main():
    import turtle
    sc1 = turtle.Screen()
    race_car5 = turtle.Turtle()
    #draw_line(100, 60, race_car)
    draw_equi_polygon(100, 6, race_car5)
    #sc1.exitonclick()

def draw_line(length, theta, turtle):
    """ draw a line with length "length", and at an angle "theta" """
    turtle.left(theta)
    turtle.forward(length)

def draw_equi_polygon(length, sides, turtle):
    """ this draws a polygon, with n sides """
    # // means integer division, this means 5//3 = 1
    theta = 360//sides
    for cur_side in range(1,sides+1):
        draw_line(length,theta,turtle)

if __name__ == "__main__":
    main()
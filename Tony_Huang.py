# please copy and paste each code seperately into your texteditor and run
# they should work indivually just fine

# Question 12

def triangular_numbers(num):
    """ program below prints out all the triangular numbers up to the num value that was passed in
    serving as the nth number place of triangular numbers"""
    index = 0
    number_start = 0
    number_add = 0

    while index <= num:
        print(number_start+number_add)
        number_start += number_add
        index +=1
        number_add +=1

    #print((20*(21))/2)
    #program ends on 210

def main():
    triangular_numbers(20)

if __name__ == "__main__":
    main()

# Question 13

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

# Question 14
# im actually just confused on how to do this one without strings and comparing char values
# so i will make it up if I can

# Question 15

# ~~ Cartesian Coordinate Points ~~

def give_me_hypothenuse(x1,y1,x2,y2):
    """ returns the distance between two cartesian coordinates """
    import math
    return math.sqrt((x2 - x1)**2 +(y2 - y1)**2)

def main():
    print(give_me_hypothenuse(0,0,3,4))

if __name__ == "__main__":
    main()
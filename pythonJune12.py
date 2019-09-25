# ~~ PRINT LINE STUFF ~~
first = "Tony"
last = "Huang"
middle = "Zhen Peng"
# this prints out Tony Huang Zhen Peng because the default seperator in python is " " (space)
print(first,last,middle)
# this prints out Tony@Huang@Zhen Peng because the seperator is now changed to "@"
print(first,last,middle, sep="@")

# ~~ RANGE STUFF ~~ 
# this gives the range from 0 - 10 exclusive, so it would be 0,1,2...9
range(10)
for count in range(10):
# by default python ends print statements with a newline, so to keep everything in one line we
# change the end of each print to ", " so we dont jump multiple lines downwards
    print(count, end=", ")
print("\n")

# this gives the range from 5 - 10 exclusive, so it would be 5,6,..,9
range(5,10)
for count1 in range(5,10):
    print(count1, end=", ")
print("\n")

# this gives the range from 0 - 10 exclusive but in steps of 2, so it would be 0,2,4,6,8
range(0,10,2)
for count2 in range(0,10,2):
    print(count2, end=", ")
print("\n")

# ~~ FUNCTIONS (methods in Java) ~~
#   def name(parameters):
#   """docstring""" #this explains what the class does, not the gritty details but general use
#   statement(s)
#   except for parameters and the "docstring" all other parts are mandatory
#   however please write the docstring

# this is the function print_pi()
def print_pi():
    """ this function prints out pi as a number (3.141592653589793) but does not return anything"""
    import math
    print(math.pi)
# this calls the function print_pi()
print_pi()


def return_pi():
    """ this function returns the value for pi """
    import math
    return math.pi

x = return_pi()
print("This will now print the variable x set to pi: ", x)

# ~~ OPERATOR PRECEDENCE ~~

# below is equivalent to x = (3^2)+2
x = 3**2+2
# prints out 11
print(x)

# below is equivalent to y = 2*(1^2)
y = 2*1**2
# prints out 2
print(y)
# the "Tony" is a string literal
# print("Tony") will print Tony, but print(type()) prints the type of whatever is in the inner ()
print(type("Tony"))

# prints the type int, since the number 2 is an int. this is called a number literal
print(type(2))

# prints the type float
print(type(2.7))

# this 2.7 is now type casted to an int which always rounds down, of course this is an int now too
print(type(int(2.7)))
# python is a dynamically typed language
# what this means is that the types of things are evaluated at run time

# python is also Strongly typed
# Strongly typed means that 'x'+5 within javascript would create a string 'x5' dynamically
#print("x" + 5)
# but in python 'x' + 5 gives us an error
# the error that pops up is: TypeError: can only concatenate str (not "int") to str

# This on the other hand are two strings, and String concatenation between two strings works out fine
print("x" + "5")
# this is what it means when it is said, Python is strongly typed

# in java we have int x = 5;
# this means that the data address for x is pointing at the value 5
# but in java we do the opposite as everything is already an object
# what I mean by opposite is that it is read left to right
# where x = 5 in python means that we get to have an object now refering to another object that-
# happens to be a int which is 5

pi = 3.141
# remember that float pi = 3.141 is the same as above BUT it doesnt actually run if actually typed
# the reason for this is that python is dynamically typed, so it reads what the object is at run-time
# and determines for itself what it thinks the type is
print(pi)

#this does not work at all
#float pii = 3.1415
#print(pii)

x = 3.141
print(type(x))
x = 3
print(type(x))
x = x+1.5
print(type(x))

# Capatlization Matters! It creates Unique Variables!
x = 1
X = 2
print(x)
print(X)

#for varaibles we use underscores for variable naming
first_name = "Tony"
last_name = "H"
print(first_name + last_name)
#prints TonyH
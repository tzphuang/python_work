x = 7
# both below will print out true as they are comparison operators
# prints true 
print(x == 7)

# prints true
print(7 == x)

# prints false
print(8 == x)

# prints true
print(x == 8 or x == 7)

# prints false
print(x == 8 and x == 7)

# prints false due to being read from left to right where the not sign 
# is assigned first to the x == 7
print(not x == 7 and x == 8)

# prints true as the inner parenthesis evaluates to false
# and after that evaluates to false, not false = true
print(not (x == 7 and x == 8))



# this will import the whole python file including the method call
# (remove the pound sign to run) import pythonTurtleJune14


def letter_Grade(number):
    """Returns the letter grade representing the number given"""
    if number >= 90:
        return "A"
    elif number >=80 and number <90:
        return "B"
    elif number >=65 and number <80:
        return "C"
    elif number >=50 and number <65:
        return "D"
    else:
        return "F"

print(letter_Grade(88))

# without pass the python compiler will give you an error
def method_in_progress():
    pass

# prints "None"
print(method_in_progress())

# ~~ ITERATORS ~~
while

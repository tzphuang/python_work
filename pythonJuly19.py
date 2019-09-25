# ~~ EXAM 2 ~~

# question 6
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1['Name'])
print(dict1['Age'])

d = {"Katy": 90, "Bob": 80 }
print(d["Katy"])

#d = {('a', 4139), ('e', 4127), ('i', 4098)}
#print(d["a"])

#d = dict((('a', 4139), ('e', 4127), ('i', 4098)))
#print(d[('a', 4139)])

#d = {"Katy": 90, "Bob": } # wrong
#print(d)

d={x: x**2 for x in (1, 2, 3)}
print(d[2])

#type(9) is int
#type(2.5) is float
#type('x') is str
#type(u'x') is unicode
#type(2+3j) is complex

def give_me_set_int(list_of_stuff):
    """this function takes in an array and only returns a set of unique integers"""
    set_int = {cur_element for cur_element in list_of_stuff if type(cur_element) is int}
    return set_int

random_list1 = ["huh", 1, 999, 101, "cool", 999, 1, 619]
print(give_me_set_int(random_list1))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

def give_set_random(length,start_range, end_range):
    """This function takes in a length, startings range and ending range
    and then it returns a set of unique integers the length of the given length"""
    import random
    set1 = set()
    while len(set1) < length:
        set1.add(random.randint(start_range, end_range))
        print(set1)
    return give_set_random

print(give_set_random(5,1,5))
print(give_set_random(10,1,11))


# Using only dictionary comprehensions and one line of code, 
# write a Python function to create a dictionary of integers of given length, 
# n and their corresponding power of given power. 
# For example for n = 9 and 
# the power of 2 your function would return  
# {1: 1, 2: 4, 3: 9; 4: 16, ...........9:81}.

def int_power_dict(length):
    """This function takes in a length, and sets it as the upperbound in a range,
    that range is then used to to iterate through each number up to and including
    the range and returns an dictionary with each number inside the range
    being the keys to its squared value, stored in its repective value"""
    power_dictionary = {index:(index**2) for index in range(1,length+1)}
    return power_dictionary

print(int_power_dict(5))


# You are given a Python list of words. 
# Write a Python function to return a dictionary of words and words count 
# using dictionary comprehension and a single line of code after function header. 

def dict_words_with_length(list_words):
    """This function takes in a list of words, sets each element of that list
    as a key in a dictionary, then for its corresponding value, sets that 
    to be the key's length """
    word_length_dictionary = {word:len(word) for word in list_words}
    return word_length_dictionary

list_of_words_use1 = ['apple', 'mango', 'banana','cherry','the ugly duckling']
print(dict_words_with_length(list_of_words_use1))


# Write a Python recursive function to calculate the sum of the following  series
# sub, 1^2 + 2^2 + 3^2 + . . + (n-1)^2 + n^2 sequence for any given n.  
# Calculate the sum for n= 10 . 
# Above sequence has a direct formula given by , 1/6(n))(n + 1)(2n + 1) . 
# So verify your results with the direct answer for n = 10.

def recursive_square_up_to_n(n):
    if n == 1:
        return 1
    else:
        return n**2 + recursive_square_up_to_n(n-1)

direct_formula_10 = ((1/6)*(10))*(10+1)*((2*10)+1)
print(direct_formula_10)
print(recursive_square_up_to_n(10))

# Write a Python class to represent a Person. 
# A person is identified by the person's name, SSN, birthday. 
# Considering all this, do the following:
# Write a Python class to represent a Person

# Write the initializer

# Make all data private

# Two persons created can be compared for identity to check whether the both are same person. 
# Facilitate this. 
# Note that same person may have different names

# Create two persons with same SSN and compare them

class Person:

    def __init__(self, SSN, name="", birthday=""): # this is the constructor of person
        self.name = name
        self.SSN = SSN
        self.birthday = birthday

    def check_same_person(self,person2): 
        # my_object.method("foo")
        # ... is syntactic sugar, which the interpreter translates behind the scenes into:
        # MyClass.method(my_object, "foo")

        return id(self) == id(person2)
            
    def __repr__(self): 
        return "Person class representing a person"


person1 = Person(123, "Bob", "01-01-1990")
person2 = Person(123, "Bob", "01-01-1990")
bob = person1
print(person1.check_same_person(person2))
print(person1.check_same_person(bob))




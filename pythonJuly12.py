# ~~ PYTHON CLASS AND OBJECTS

# ~~ PYTHON CLASSES/ INHERITANCE ~~
# within the real world we have inheritance
# and real world objects that inherit are usually classed into parent-child relations
# these relations are more specific as you go down a heirarchy
# so for example we have a "car" 
# a very generic term but specific enough to know what it is
# but there are cars such as gas cars/ electric cars
# this is a "specialized" car 
# so this would be a child of the more general "Car"
# so as we go down in a hierarchy we are "specializing", kind of fine tuning a specific idea
# but as we go up a hierarchy we are "generalizing", kind of lopping off the extra features
# where we go back to the base model

# ~~ PASSING CLASSES/ FUNCTIONS TO THE CHILD ~~
# so just like Java we have inheritance where we reuse code from the parent
# as we make children classes that inherit not just code but features, its parent's has
# remember with inheritance, a electric car "IS" a car, but a car may not necessarily
# "IS" a electric car
# these sub classes, sometimes called derived classes, child class, extended class
# as it is a derivative of the original

# ~~ SUPER CLASS ~~
# the class from which a subclass is derived is its parent, or in inheritance terms
# it is its SUPER class

# in python we practice inheritance as follows
# class DerivedClassName(BaseClassName):
#   <statement -1>

# ~~ EXAMPLE OF INHERITANCE ~~
class Book:

    def __init__(self, title="", author="", isbn=""): # this is the constructor of book
        self.title = title
        self.author = author
        self.isbn = isbn

        # getters
        # setters
        # ...etc

    def __repr__(self): 
        #object.__repr__(self): called by the repr() built-in function and 
        # by string conversions (reverse quotes) to compute the "official" string 
        # representation of an object.
        # object.__str__(self): called by the str() build-in
        # function and by the print statement to compute the "informal"
        # string representation of an object.
        return "Book class representing a book"

# ~~ this is too much repeated code ~~
# ~~ so instead we use the inheritance feature of object oriented programming ~~
# to do some of the legwork
#class Textbook(Book):
    # pass
    #def __init__(self, title="", author="", isbn="",subject=""): # Constructor of Textbook
        #self.title = title
        #self.author = author
        #self.isbn = isbn
        #self.subject = subject



# ~~ here we have the above code but using inheritance instead ~~
class Textbook(Book):
    # pass
    def __init__(self, title="", author="", isbn="",subject=""): # Constructor of Textbook
        Book.__init__(self, title, author, isbn)
        self.subject = subject

    def __repr__(self):
        return "Texbook class representing a Textbook"





text_book1 = Textbook()
text_book2 = Textbook("Python", "ISW", "777", "Excellence with Python")

print(text_book1) # prints its def __repr__(self): statement
print(text_book2)
print(text_book2.title)

# EVERYTHING INHERITS FROM OBJECTS
s3 = object()
print(s3)

# Java has a single parent class
# PYTHON YOU CAN INHERIT FROM MORE THAN ONE CLASS
# so a sub-class can have multiple parents

# java has abstract classes
# python also still has it called import ABS

# Question 2
#Group assignment:
#Extend Python's string class to represent a string literal only in a floating point number format.
#Add methods to convert the literal to the corresponding  floating point number, 
#to convert to an integer number and to split the literal into parts based on a given delimiter
#which default to "." character. 
#Copy paste your code here:
class num_string(str):
    # no need for initializer
    # def __init__(self, strang)
    #   self.strang = strang

    def to_int(self):
        return int(float(self))
    def to_float(self):
        return float(self)
    def split_float(self, delimeter = "."):
        return super().split(delimeter) 
        # the super here only works because num_string is a child of the "str" class
        # in this case it would be the (string).split(delimiter) method
        # return str(self).split(delimiter)

string_float1 = num_string("123.456")

print(string_float1.to_int())
print(string_float1.to_float())
print(string_float1.lower())
print(string_float1.split())



# Question 3
#Create a Python class to represent a Pet. A pet is uniquely identified by its name, 
#its owners name its tag number. A Pet also have an age.

class pet: #this is where you would inherit if you wanted to do that
    def __init__(self, age, name="", owner_name="",tag_number=""): #default parameters go at the end
        self.name = name
        self.owner_name = owner_name
        self.tag_number = tag_number
        self.age = age

    def __repr__(self): #tells the USER who is calling this class what, this OBJECT represents
        return "This is a pet class object"

#Create another class to represent a mammal.  
#Mammal has a description of what are mammals and specify 
#how many mammals species have been found so far. 

class mammal:
    def __init__(self, amount_found, description=""): # default parameters go at the end
        self.description = description
        self.amount_found = amount_found

    def __repr__(self):
        return "This is a mammal class object"


#Write Python classes to represent a Pet and a Mammal. 

#A Dog is a Pet. as well as a Mammal. 
#A dog can be uniquely identified by its name and owners name  and the tag name. 
#A dog also has the field, breed and state whether the dog is sterilized or not.
#Write a Python Dog class that extends both from Pet and a Mammal. 

class dog(pet, mammal): # dog object inherits from pet & mammal parent classes
    count = 0 # this is a static variable as it is outside the actual instanced
              # variables of an object
    def __init__(self, tag_num, breed, sterilized, dog_name, owner_name):
        count += 1 # updates the total dogs registered to the clinic (this activates everytime
                   # the initializer is called for dog, so the static count variable for
                   # the total counter for the class dog is incremented by 1)
        pet.__init__(self, age, dog_name, owner_name, tag_num)
        mammal.__init__(self, amount_found, description="")
        self.breed = breed



#A veterinary clinic is going to use these class hierarchy for their use. 
#Add a way to count all the dogs going to get registered (created) in the clinic. 
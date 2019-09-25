# ~~ Strings ~~
fruit = "apple"
# prints out the stored string "apple"
print(fruit)
# since the variable fruit is now type "string" it will print class 'str'
print(type(fruit))

# letter is now a string that holds "p"
letter = fruit[1]
# prints "p"
print(letter)
# prints string as the type
print(type(letter))


#remember that shift+command+left selects whole line to the left of cursor
#remember that shift+command+right selects whole line to the right of cursor

# ~~ STRING AND LEN FUNCTION ~~
# the len function retrieves the length of a string and returns it as
# an integer
length = len(fruit)
# prints the integer 5
print(length)
# prints the class "int" due to python being dynamicly typed
print(type(length))

# recall that strings start with the 0th term up to length-1
# so for the string fruit the 0th term is "a"

# ~~ TRANSVERSAL THROUGH A STRING ~~
# run through the length of the string "fruit" using a for loop
# starting at 0, going to length-1, and then printing each one
# prints out a, p, p, l, e, 
for count in range(0,len(fruit)):
    print(fruit[count], end = ", ")
print("\n")

# this does the same as the above but using a while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter, end = ", ")
    index = index+1
print("\n")

# this also does the same thing above but in a very simple for each loop
# the dynamic string storing each letter of fruit can be anything
# here it just happens to be "character"
# and since the range in this case is a string, the for loop will go through the whole thing
for character in fruit:
    print(character, end = ", ")
print("\n")

# ~~ STRING SLICES ~~
s = "Monty Pyton"
# below prins the out the substring using the string slice method
# s <- the string s[(inclusive),(exclusive)]
# the slice will print out the inclusive first part but not print out the last indexed exclusive part
# prints out Monty
print(s[0:5])
# prints out Python
print(s[6:12])

# if you omit the first index before the colon the slice starts at the beginning of the string
# if you omit the second index after the colon the slice ends at the end of the string
# next two line does the same as above
print(s[:5])
print(s[6:])
# what does this do?
# starting the slice at index 3 of string s and ending it with slice 3 exclusive
# well it prints nothing, an empty string ""
print(s[3:3])
# what does this do?
# well since both the beginning and the end index of slicing are not given
# we will start at the beginning, and end at the end of the string
print(s[:])

# ~~ STRINGS ARE IMMUTABLE ~~
greeting = "Hello, World"
# Below does not work because strings are immutable
# it will return the message TypeError: 'str' object does not support item assignment
# the reason for this is once a string is created
# it may not be changed
# greeting[0] = "J"  //this is commented out due to causing an error

# but we can get around this by being clever with our code and doing what would be the same
# below the code new_greeting is a new string that holds a string of "J" concatenated with 
# the greetings string slice starting at index 1 (inclusive) to the end of the string
new_greeting = "J" + greeting[1:]
# prints out Jello, World
print(new_greeting)

# ~~ LOOPING AND COUNTING ~~
# below are variables being set
word = "cucumber"
count = 0
# the code below creates a for loop and using letter as a string
# assigns each letter within word to letter one at a time with each iteration
# and uses that to compare if it is logically equal to the string "u"
# if it us, then count goes up by 1
# if not the program does nothing
for letter in word:
    if letter == "u":
        count += 1
# prints the number of "u" within "cucumber"
print(count)

def letter_Counter(letter_I_want, main_String):
    counter = 0
    for letter in main_String:
        if letter == letter_I_want:
            counter += 1
    return counter
# below prints out 4 due to having 4 g's within the string "gangster paradise gangsteriso"
print(letter_Counter("g","gangster paradise gangsteriso"))

# ~~ THE IN OPERATOR ~~
# the in operator takes the first string and returns true if it appears as a substring
# within the second string
# this returns true
print("a" in "banana")
print("toad" in "toad-be-gone")
# this returns false
# returns false because upper/lower case matter
print("CrAZy" in "Crazy like a fox")
# returns false because \n (new line) counts
print("cool" in "co\nool")

# ~~ STRING COMPARISON ~~
# the comparison operator == works on strings

print("excellent" == "excellent")

word = "cool beans"
if(word == "cool beans"):
    print("Noice beans")

# the other comparison operators also work with Strings and they can be used for
# putting strings in alphabetical order

def compare_to_beans(word):
    if word < "cool beans":
        print("Your word \"" + word + "\" comes before \"cool beans\"")
    elif word > "cool beans":
        print("Your word \"" + word + "\" comes after \"cool beans\"")
    else:
        print("Noice beans")

compare_to_beans("apple pie")
compare_to_beans("cool beans")
compare_to_beans("watermelon soup")

# ~~ STRING METHODS ~~

thingy = "Hello Earth"
print(type(thingy))
# the dir function, lists method avaliable to the object within the parenthesis
# below prints out the entire list of methods for the object thingy which is a string
# so below prints out the entire method list for strings
#print(dir(thingy)) //commented out due to large amounts of written code
# help specifically tells you what the method does and how to use the method in a simple
# few lines, where it describes what the method does
#print(help(str.capitalize)) //commented out due to large amounts of written code

word = "alan walker"
# calling a method is similar to calling a function
# but methods are specificly made to a variable
# while functions usually are stand alone
# when using methods we use the dot notation, where we append a .(method)() onto the back of
# an object that has that method
# in this case we use "word" which is a string, add the .upper()
# this returns the uppercase version of "word" as a string
# a method call is called an "invocation", we would say we are invoking "upper" on "word"
word_cap = word.upper()
print(word_cap)

word = "crap shoot"
# the find method, finds the first substring of "oo" and prints out the starting index
# of where it would start
index = word.find("oo")
# this prints 7, where "oo" would start in the string "word"
print(index)

# this is an overloaded method that can take multiple varaibles
# in this case 1, 3 signify different things
# 1 signifies the start of finding a word(inclusive), so itll start at index 2 within "word"
# 3 signifies the end of finding a word(exclusive), so itll end on index 3 but not acknowledge it
# since "crap shoot" = [c][r][a][p][ ][s][h][o][o][t]
# and we are finding "rap" within [r][a]
index = word.find("rap", 1, 3)
# since there is no "rap" in "ra", it prints out -1
print(index)

# .strip removes white spaces from the beginning and ending from a string
line = "    here we go again    "
print(line)
print(line.strip())

# .startswith takes in a string and sees if the object (in this case "line") starts with
# whatever the argument string is
line = "What did you say to me, you"
# prints true
print(line.startswith("What"))
# prints false, as capatilziing matters
print(line.startswith("w"))

# ~~STRING PARSING~~
data = "For the fairest: thuang54@mail.ccsf.edu, we applaud you"
first_position = data.find(": ")
print(first_position)
end_position = data.find(", ")
print(end_position)
email = data[first_position+2:end_position]
print(email)

# ~~FORMAT OPERATOR~~
camels = 42
print(type(camels))
# the formating operator is  the % sign, in math it is the modulus key but in python
# using strings it is used as the formating key
# %d to format integers
# %g to format floating point numbers
# %s to format strings
# essentially it replaces each following format operator with the next element
print("I have %d camels in my stables" % camels)
# the number of formatted operators and each type of formatted operator must match
# to its corresponding replacement
print("In %d years I spotted %g %s" % (3, .5, "trucks"))

# ~~ OPERATION ON STRINGS ~~
# remember that strings are immutable but that doesnt mean we cant concatenate them together
message = "shut your face"
print(message + " before i make you")
# multipling lines is easy within python
# you just add the * key to whatever you want 
# parenthesis rules, and arithmetic rules still apply
# multiplication goes first before addition
# prints "Power Rangers Go Go Go ""
print("Power Rangers " + "Go " * 3)
# prints "Power Rangers Go Power Rangers Go Power Rangers Go "
print(("Power Rangers " + "Go ") * 3)

# ~~ INDEX OPERATOR: WORKING WITH CHARACTERS IN STRINGS ~~
# recall that strings are just multiple one string put together
school = "galileo"
# left to right we get 0,1,2...length-1
letter_g = school[0]
print(letter_g)
# right to left we get -length...-3,-2,-1
letter_o = school[-1]
print(letter_o)

line = "Hello World"
# counts number of "l" in the string line
number_of_l = line.count("l")
# prints the number
print(number_of_l)
# replaces every instance of "World" with "*****" 
# due to no 3rd parameter, it will replace all occurences
line_censored = line.replace("World", "*****")
print(line_censored)

# ~~ STRING FORMAT METHOD ~~
# formating things is just like fill in the blank with whatever you want
person_name = "fungus chungus"
# this works too
# person_name = input("Your name: ")
greeting = "Hello {}".format(person_name)
print(greeting)

# a more comlpex way of doing things
original_Price = float(24.99)
discount = float(8.5)
# this means that if multiplied to the original price, the original price
# would become 91.5% of what it would be originally
new_price = (1-(discount/100))*original_Price
# this formating rounds up due to the .2f formating choices
# so it will round to the nearest penny always
calculation = "${:.2f} discounted by {}% is ${:.2f}.".format(original_Price, discount, new_price)
print(calculation)

# ~~STRING COMPARISON CONTINUED~~

# what if I compare apple and Apple?
# prints false
print("apple" < "Apple")
# prints false
print("apple" == "Apple")
# prints true
print("apple" > "Apple")

# why does this happen?
# this happens because of the letters we use are assigned a number in the background
# signifying their order, this so-called "ordinal value" is what defines what comes first
print(ord("a"))
print(ord("A"))
# ordinal value for "a" is 97
# while the ordinal value for "A" is 65

# you can also reverse this by the chr method
print(chr(97))
print(chr(65))
# below prints the blank space
# \" is to escape the default recognition of the quote key and recognize it as a literal
print("\""+chr(32)+"\"")

# ~~ 9.10 TRAVERSAL AND THE FOR LOOP: BY ITEM ~~
# for each element within the square brackets, the for loop stores it in the place variable
# then iterates through all the elements while printing through each iteration of the for loop
for place in ["here", "there", "nowhere", "dont care"]:
    line = "I " + place + ", there"
    print(line)

# prints all numbers in range
for avalue in range(10):
    print(avalue, end = ", ")
print("\n")

# this prints all the things in the range from 0 - 20, at 5 steps increments
# the start is at 0 which is inclusive, so 0 prints no matter what
# then you go up 5 steps which ends on the integer "5" then it prints that, etc
# but it doesnt print 20 as it is exclusive for the end
for number in range(0,20,5):
    print(number)

# runs through the each element in the string 
# (basically each element only holds another string, that each hold a single character)
# and then it loops through print each
for character in "Prints each character in the element":
    print(character, end = ", ")
print("\n")

# this will print repeat 5 times, since starting at 3 inclusive, and ends at 8 exclusive
# for s[3:8] this means that we will be reading the string "s" left to right starting at index 3
s = "python rocks"
for ch in s[3:8]:
    print("repeat", end=", ")
print("\n")

# ~~ TRAVERSAL AND THE FOR LOOP: BY INDEX ~~

# starting at 0 to the length of string "fruit" (length is 10)
# we use each new index which is the previous index value+1
# and iterate through the fruit string
fruit = "watermelon"
print(len(fruit))
for index in range(len(fruit)):
    print(index, end = ", ")
    print(fruit[index], end = ", ")
print("\n")

# starting at index[fruit length -1] which is index[9]
# we then increment the index by -1 each step
# we end the for loop when the range is -1 (exclusively), which means that
# we have fruit[length-1], fruit[length-2] ... fruit[1], fruit[0]
# and then it stops there because it excludes fruit[-1]
for index in range(len(fruit)-1,-1,-1):
    print(fruit[index], end = ", ")
print("\n")

# ~~ TRAVERSAL AND THE WHILE LOOP ~~

# simple while loop with index starting at 0 up to length(exclusive)
index = 0
while index < len(fruit):
    print(fruit[index], end = "|")
    index += 1
print("\n")

# ~~ THE IN AND NOT IN OPERATORS ~~
# THIS SHOULD NOT BE CONFUSED WITH THE FIND METHOD
# IN, AND FIND ARE COMPLETELY DIFFERENT THINGS IN PYTHON
# IN, CHECKS IF A STRING IS "IN" ANOTHER STRING
# FIND, WILL FIND A STRING WITHIN ANOTHER STRING, AND RETURN AN INTEGER ONCE IT KNOWS ITS STARTING-
# LOCATION AND IF IT DOESNT FIND IT, IT WILL RETURN -1

# prints true because "ga" is in the string
print("ga" in "ggjgekjglkgjalgjlejgaljalgjalgej")
# prints false because to be true, what would have to not be in the string
# so since it is in the string, it is false
print("what" not in "what, huh?")

# ~~ THE ACCUMULATOR PATTERN WITH STRINGS ~~

def remove_vowels(string):
    """ takes in a string, and stips it of every vowel wether it is uppercase or not """
    vowels = "aeiouAEIOU"
    new_string_no_vowels = ""
    for current_char in string:
        if current_char not in vowels:
            new_string_no_vowels = new_string_no_vowels + current_char
    return new_string_no_vowels

print(remove_vowels("Computer Science Is The BEST"))

s = "ball"
r = ""
for item in s:
    # here we have a problem
    # the r is being concatenated after the new character is upper cased
    # so the iterations look like
    # "B"
    # "A + B"
    # "L + AB"
    # "L + LAB"
    # thus turning it backwards "LLAB"
    r = item.upper() + r
print(r)

def count_of_letter(letter, string):
    """ counts the number of letter inside string and returns that number of time it shows up """
    counter = 0
    for char in string:
        if char == letter:
            counter += 1
    return counter

print(count_of_letter("h", "hippohatohus"))

# ~~ A FIND FUNCTION ~~
strang = "hopey shat, bathmon"
string = "pey"
# below is the syntax to call the string find method
# it is a method for strings so it uses the .method format
# it takes in a string as a parameter, which is the "string"
# that we are looking for within the current string object we have
# it then prints the position of where the sub string we are looking for starting index
print(strang.find(string))

# ~~ CHARACTER CLASSIFCATION ~~
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
print(string.__all__)


# ~~ OPTIONAL PARAMETERS ~~ 
def optional_method(string, char, strang = None, index = -1):
    """ this function takes in a string and a char and searches the string if it has the char
    if it doesnt have the "char", we then see if "strang" is not "None", and if it isnt, we search
    the original string if it has the sub string "strang" """
    if char in string:
        index = str(string.find(char))
        print("char is currently found at index: " + index)
    elif not (strang == None):
        if strang in string:
            index = str(string.find(strang))
            print("strang is currently found starting at index: " + index)
        else:
            print(str(index))

# here is the default method call to "optional_method"
# this then prints out the position of the first instance of "u"
optional_method("some string that I used to know" , "u")

# here is the call to the same method but this time, z is not in the string, so the backup
# "string" is used and see if its inside the original string
# which it is, so it prints out the starting index of the word "string"
optional_method("some string that I used to know" , "z", "string")

# here we call the same method again this time with a backup string that cannot be found
# this means that the "char" and backup string are not substrings of the original string
# this prints out the index -1
optional_method("some string that I used to know" , "z", "NOT_FOUND")

# here we have a method call with all the parameters filled, so it takes over all the defaults
# that were orginally set, but since both the "char" and backup string are still not found
# we have return the index which was originally -1, but since it was overwritten with 8
# which was passed in as the parameter, it will now print 8
optional_method("some string that I used to know" , "z", "NOT_FOUND", 8)

# is there a way if I had put the index -1 before, strang = None to make it so that I would 
# not pass anything into it? something like below?
# optional_method("some string that I used to know" , "z", "NOT_FOUND",(nothing parameter), EXTRA_PARAMETER_HERE)

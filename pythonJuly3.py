# ~~ LISTS again ~~
# lists are collections of elements that can be different types of elements
# in python unlike java, where you can have integers, strings, and even
# have other sublists within a list together at a time
# for example
list_of_everything = ["sup", 10, 5.4, ["sublist", 11, 5.5]]
print(list_of_everything)

# Remember that calling elements of a list you use their index, starting from
# the first element of that list at 0, and going to the last element which is length-1
# so to print out the last element of the list I would take the length-1 which is 4-1 =3
# and call it
print(list_of_everything[3])
# this prints out the element of list element index 3, which is the 4th element of the list
# and this item is a list itself so it prints out the enitre list

# we can also call elements of the list starting from negative values just like strings
# where the negative values start at the last element working right to left
print(list_of_everything[-1])
# above is the same as printing the last element in the list

# to print out the length of a list we use the function len(list)
print(len(list_of_everything))
# this prints out the value 4

# so to get the first element of the list, you would have to get the negative of list's length 
print(list_of_everything[-(len(list_of_everything))])
# this will then print out "sup"

# you can also apply methods to elements of a list as if they were just the elements themselves
print(list_of_everything[0].upper())
# this grabs the first element of the list, and since it is a string we can uppercase it 
# using the string method .upper()

# you can also go into sub lists/strings with second list
#  bracket "[]"
print(list_of_everything[0][2])
# this prints out p, which is the the 1st element of list_of_everything,
# and the 3rd element of the string "sup"

# you can also use the "in" and "not in" boolean operators to check membership within
# your lists just like you would with strings

my_string = "what did you say to me mother-"
print("what" in my_string)
# examples using strings above, which does print true
# since the sub string "what" is in my_string

# below is the example with lists
print("sup" in list_of_everything)
# "sup" is a member of list_of_everything

# below is an interesting thing about sub lists
# here we have a sublist sub_list_test pointing at the sublist within list_of_everything[3]
# this means that each pointer is at the same address
# so it would logically mean that if the memory address stored in sub_list_test
# is the same pointer, it would be "in" the list list_of_everything
sub_list_test = list_of_everything[3]
print(sub_list_test in list_of_everything)
# which is true

# "not in" example
print("Sup" not in list_of_everything)
# the string "Sup" is "not in" the list "list_of_everything", so it evaluates to true

# also remember that sublist
# s dont take into account into the check with in
# only the surface level list
#  is evaluated
alist = [1,2,3,4,5,[6]]
print(6 in alist)
# this evaluates to false as the element of alist[5] is not taken into account,
# only the address of the list that holds the integer 6 is 

# You can concatenate and repeat things in list
# s just like strings
# for example

odd = [1,3,5]
even = [2,4,6]
# shoves both elements in each list
#  into a single list
#  starting from left to right
print([1,2] + [3,4])

# concatenates each list
#  from left to right
print(odd + even)
print(odd + [7,9])

# concatenates the list
#  that is repeated with itself 3 times into a single list

print([7] * 3)

# concatentates the list
#  "alist" with itself 2 times into a single list

print(alist * 2)

# ~~ LIST SLICING ~~
# the slice operation is the same as we saw with strings, and it works with lists also!
a_fabulous_list = ["a", "b", "c", 'd', "e", 'f']
# remember that the first element is inclusive, and second is exclusive
# [(inclusive):(exclusive)]
# prints full list
print(a_fabulous_list[:])

# prints list up to element 3 but not element 3
print(a_fabulous_list[:3])

#prints list up starting at element 3 to end of list
print(a_fabulous_list[3:])

# ~~ MUTABILITY AND LISTS ~~
# lists are changable! they are not set in stone
fruit = ["apple", "banana", "orange"]
print(fruit)
fruit[0] = "rotten_apple"
fruit[-1] = "peach"
print(fruit)
# you can also change multiple parts of a list at once!
alist = ["a", "b", "c", "d", "e", "f"]
print(alist)

# here we change the above list's index1/index2 elements to x and y respectively
alist[1:3] = ["x", "y"]
print(alist)

# here we can also replace certain elements of the list with no list at all
# essentially deleting them from the list!
alist[3:] = []
# so starting at index3 inclusively, we replace it and all elements that follow with an empty list

print(alist)

# ~~ DELETION WITHIN LISTS, AND LIST DELETION ~~
# using slices to delete lists can be really awkward as remembering inclusivetivity and
# exclusivetiviy of the elements can be problematic
# so instead we an alternative with the "del" statement which does the same
muh_listo = ["one","two","three"]
print(muh_listo)
del muh_listo[1]
print(muh_listo)

alist = ["a", "b", "c", "d", "e", "f"]
del alist[1:5]
print(alist)

# mutability and lists problems that occur due to the nature of the idea of
# objects and references

a = "banana"
b = "banana"
print(a is b)
# this prints true as both a and b refer to the same string "banana"
# as theyre refering to the same object address

# but for lists, its different, as shown below
a = [81, 82, 83]
b = [81, 82, 83]
print(a is b)
print(a == b)
# The reason why a is b false and a == b is true is because 
# a is b compares the references to the list of objects
# but a == b compares all the individual values of the list

# and since the indivual list
#  elements of the are the same (as shown below)
print(a[0] is b[0], a[1] is b[1], a[2] is b[2])
# we know that the values are the "same"
# but why is "a is b" false?
# well this has to do with how collections work in python
# we have the collection of [81, 82, 83] and then assign that collection to "a"
# that collection is uniquely addressed
# and then again [81, 82, 83] is now assigned to "b" which creates another unique address
# that is how python works
# but why is the values all the same? for each element? Why do they have the same addresses?
# well that is because to save memory, python will take integer objects, and similar things
# and let them be shared
# this in turn leading the the next topic "aliasing"

# ~~ ALIASING ~~
# aliasing, when you assign two references to the same address
a = [1,2,3]
b = a
# both references hold the same address so "a is b" and "a == b"
# a is b refers to the referenes sharing the same address
# while a == b refers to the two reference's elements sharing the same address(es)
print(a is b)

# ~~ CLONING LISTS ~~
# you can clone lists with slicing
a = [1,2,3,4,5]
b = a[:] # this copies each indivual element into a list with "b" referencing it
b[0] = 0
print(a)
print(b)
# "a" and "b" are not aliases

# ~~ REPETITION AND REFERENCES ~~
original_list = [45, 76, 34, 55]
print(original_list * 3)
# this will print the original list 3 times back to back in a single list

# below is the same as above
changed_list = original_list * 3
print(changed_list)

# below is not the same as each iteration of original_list is now a sub list

changed_list = [original_list] * 3
print(changed_list)
# now that each element within change_list is a sub list
#  that contains a reference to original_list
# we get problems like
original_list[1] = 99
print(changed_list)
# this.
# the problem here is actually quite simple, you have a reference to a reference to a value
# if you change the middle man, you change what the first reference sees, in this case
# changed_list references 3x original_list, and that references indivual integers
# when you change original_list, you also change changed_list (whether on purpose or not
# I have no idea)

# ~~ LIST METHODS ~~
# appending adds a new element at the end of the list
# .append(element) - no return value
here_comes_the_list = []
here_comes_the_list.append(5)
here_comes_the_list.append(27)
here_comes_the_list.append(3)
here_comes_the_list.append(12)
print(here_comes_the_list)

# .insert((index), (element)) - no return value
# inserts an element into the list at specified index
here_comes_the_list.insert(1, 12)
print(here_comes_the_list)
here_comes_the_list.append(12)
print(here_comes_the_list)

# .count(element) counts how much elements there are of "element" - returns an integer
print(here_comes_the_list.count(12))

# .index(element, start(inclusive), stop(exclusive)) 
# .index() - returns back the first index in which the "element is see in thea list
# "
# we can even specify the start and stop of the indexes
# the index start is inclusive, so it starts on that index
# the index end is exclusive, so it ends right before that index
print(here_comes_the_list.index(12))
print(here_comes_the_list.index(12,2))
# returns an error
# print(here_comes_the_list.index(12,2,4))

# .reverse() reverses the list
# - no return value

here_comes_the_list.reverse()
print(here_comes_the_list)

# .sort() sorts the list from least to greatest (at least with integers)
# - no return values
here_comes_the_list.sort()
print(here_comes_the_list)

# .remove() removes an item by ELEMENT, by first seen first to go
here_comes_the_list.remove(12)
print(here_comes_the_list)

# .pop()
# this will return and then delete the last element in the array
print(here_comes_the_list.pop())
print(here_comes_the_list)

# .pop(index)
# this will return and delete the element at index insie the array
print(here_comes_the_list.pop(1))
print(here_comes_the_list)

# ~~ APPENDING VS CONCATENATING
Thor_List = [7,7,7]
print(Thor_List)
Thor_List.append(7)
print(Thor_List)
Thor_List.pop()

# as shown below concatenation and appending do the same thing on the surface
# where they add things at the end of the list
Thor_List = Thor_List + [7]
print(Thor_List)
# but the difference is more subtle where concatenation creates another memory address
# where you can have two lists with concatentation
# but with appending you are only ever modifying an existing lists

Loki_list = Thor_List +[6]
print("original list" , Thor_List)
print("new memory address" , Loki_list)

# NOTICE, you can only concatenate lists to lists
# Thor_List = Thor_List + 7 does not work
# Thor_List = Thor_List + [7] does work

# ~~ LISTS AND for LOOPS 10.17
# list transversal is quite easy in python
# you can do it by index, or by elements
# where as in java you only get to do it by index

fruits = ["apple", "orange", "banana", "cherry"]
for current_fruit in fruits: # this for loop does list transversal by element
    print(current_fruit, end = ", ")
print("\n")

# since the start is not stated, len(fruits) is the maximum index the range will go to
# starting at 0
# so it would be 0, 1, 2, 3 but not actually include index 4 as it is exclusive
for current_index in range(len(fruits)): # this for loop does the list transversal by index
    print(fruits[current_index], end = ", ")
print("\n")

# ~~ USING LISTS AS PARAMETERS ~~
# when you pass in lists as paramenters into a function call
# and using that list we modify the elements of that list, we call that "modifiers"
# when that happens we get a new list, and the changes to that list is called a "side effect"

# ~~ PURE FUNCTIONS ~~ 
# A pure function on the other hand unlike modifiers will not produce any side effects
# this means that anything that specific function does will not "change" any of the 
# elements that were passed in as parameters but instead will use the passed in elements
# to be used by the function and then return something of value created based on
# the functions use, and parameters passed in

# SO WHY CARE? AND WHICH IS BETTER?
# well to begin with, anything you can do with modifiers, can also be done with pure functions
# this means what we as programmers have a choice
# this also means that one will be better than the other in certain situations
# pure function programs, are said be faster to develop and are less error-prone
# but modifiers are convient at times and totally pure function programs are less effiencient
# so it is recommended to try writing things in a "pure function" type of way but if you have to
# then use modifiers
# this approach to programming is called "functional programming style"

# ~~ LIST COMPREHENSIONS ~~
# list comprehensions is a way to get a list returned back after being passed as a parameter 
# and based on some condition it will process the elements with that condition in mind
# [<expression> for <item> in <sequence> if <condition>]
# the if <condition> is not necessary as it is not mandatory to have
# for example
my_list = [1, 2, 3, 4, 5]
your_list = [item ** 2 for item in my_list] # list comprehension on the right side
print(my_list)

# the list comprehension here essentially does
# goes through each element in the array my_list
# takes each item and squares it, then adds it as a new element in a list since the
# elements are within [] (brackets) this means that what is returned is a whole new list!

# example of a bigger, badder list comprehension
super_list = list(range(1,101)) # this creates a list form 1(inclusive) - 101(exclusive)
only_divisible_3 = [number*1 for number in super_list if number%3 == 0]
# [number*1 for number in super_list if number%3 == 0]
# for each element in suer_list, if it is divisible by 3 with no remainder, that number*1
# will be an element of the list, only_divisible_3
print(only_divisible_3)


# ~~ NESTED LISTS ~~
# just like in java, you start with the outter list first then go in
# [surface level list][1 level inside surface level list][1 leve inside list to the left][etc]..

ugly_list = [["a", "b", "c"], [True, False]] # [[1,2,3], [4,5,6], 7,8,9 [7,7,7]]
if ugly_list[1][0]:
    print(ugly_list[0][2])
else:
    print(ugly_list[1][1])

# ~~ STRINGS AND LISTS ~~
# a really good method to keep in mind when using lists, and strings is the "split" method
# the method breaks strings in a list of words using the white space as the word boundaries
# for example
phrase_1 = "holy cow the holy milk produced by this holy animal is gross"
phrase_1_list = phrase_1.split()
print(phrase_1_list)
# you can also set the delimiter of the splitter to not default on white space
# but instead on something you choose
# lets say you have the word "holy"
phrase_1_list2 = phrase_1.split("holy")
print(phrase_1_list2)
# too bad this doesnt actually get rid of the blank spaces too, or can we?
print((phrase_1.replace("holy", " ")).split())
# here we replaced "holy" and " " where I used the default on the split method
# and just replaced all iterations of "holy" with " " and split sweeped up the rest
# of the added blank spaces

# below is a way to use built in functions to split on certain key characters
# a='Beautiful, is; better*than\nugly'
# import re
# print(re.split('; |, |\*|\n',a))
# below is than printed out
#['Beautiful', 'is', 'better', 'than', 'ugly']

# ~~ LIST TYPE CONVERSION FUNCTION ~~
# python has a built in conversion function TO CREATE LISTS OUT OF ANYTHING
# for example
gits_quote = "When I was a child, my speech, feelings, and thinking were all those of a child..."
list_gits_quote = list(gits_quote) # when you create a list of a string, it breaks it up into its indivual elements
print(list_gits_quote) # this prints out each character as an element in the list "list_gits_quote"

# gits_quote.split() THESE TWO
# list(gits_quote) ARE NOT THE SAME
# .split() will split via white space
# list("string") will split each character

# ~~ TUPLES AND MUTABILITY ~~
# tuples are like lists, in python
# but the difference is that lists are mutable, where you can change the memory addres of the list
# while tuples, you can not change the memory address of that 
# once a tuple is created, it cannot be changed, where its items cannot be changed
# usually you use tuples for "records", records are some related information
# that happen to belong together
# tuples are generally created with parenthesis with elements seperated by commas
tony_traits = ["awesome", "excellent", "superb", "extraordinarily", "humble"]
print(tony_traits)
tony_traits[0] = "asshole"
print(tony_traits)

tony_traits = ("awesome", "excellent", "superb", "extraordinarily", "humble")
print(tony_traits)
# tony_traits[0] = "asshole"
# TypeError: 'tuple' object does not support item assignment

# so if you cant change tuples outright, can you do some fancy magic to still change them?
# the answer is YES
# its not too fancy either, its just concatenation
tony_traits = tony_traits[:3] + ("I", "too", "am") + tony_traits[3:]
print(tony_traits)

# also side note, single element tuples are created like this
tuple_one_element = (1,) # YOU HAVE TO HAVE THAT COMMA WITH SINGLE ELEMENTS
print(type(tuple_one_element))
print(tuple_one_element)

# without the comma with single elements python instead reads the parenthesis as math
# and (1) is just 1 in math
tuple_not_one_element = (1)
print(type(tuple_not_one_element))
print(tuple_not_one_element)

# ~~ TUPLE ASSIGNMENT ~~ 10.27
# tuple has a great assignment feature where it can easily.. wait a fucking minute
# doesnt this break tuples? WHAT THE EVER LOVING FUCK
# they are immutable but they can be element assigned???
# ask teacher on monday cause this is dickcheese

#print((name, surname, birth_year, movie, movie_year, profession, birth_place) = julia)
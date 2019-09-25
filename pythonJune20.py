a_string = "monty python"
print(a_string[::-1])

# ~~ python lists ~~
# why make lists in python? 
# python lists are very versatile as they can handle more than one data value
# each data value is sequential, where each value is identified by their index
# each item in a list, is called an element
# in simple terms, a list is a list of objects
# strings are immutable, while lists are mutable (except for tuples)

# simple lists
[True]
[1,2,"python",2.5]
empty_list = []


# builts in list function list()
alphabet_list = list("abc")
list3 = list(range(10))
list4 = "Python Programming".split()
list5 = [1,2,[2,3,"a"],4,5]

def print_list(list):
    """ will print the list's elements """
    for char in list:
        print(char, end = ", ")
    print("\n")

print_list(alphabet_list)
print_list(list3)
print_list(list4)
print(len(list5))
print_list(list5)

# prints the first element in list4
print(list4[0])
# prints the 3rd element of the 3rd element of the array list5
print(list5[2][2])
# prints the right most element in the list4
print(list4[-1])

# ~~ slicing ~~
# [n:m]

# below is one of the problems that comes with references
# this problem is mutability
# since python objects are references, we get "aliasing"
# two object references, that refer to the same object
alist = [4, 2, 8, 6, 5]
blist = alist
blist[3] = 999
print(alist)

# below we have the deletion of an element within the array
# we delete the item at the first index, which is the second element
a = ['one', 'two', 'three']
del a[1]
print(a)

# concatenation
print(list3 + list4)
# multiplication of lists
# will print the enter list of objects within the list and then go back to the beginning of the list
# 2 more times, making a print line of 3x list4 back to back
print(list4 * 3)

# id funtion for python objects is the "reference address"
# if two objects refer to the same thing what does that mean?
# both of those objects are aliases, and are able use the SAME object
print(id(list4))
# the id for list4 is 4525907912 

alist = [1,2]
blist = [1,2]
# this compares the ELEMENTS inside each list which is true
print(alist == blist)
# the "is" function compares the id of the lists which is false, they have different ids
print(alist is blist)

blist = alist
# this compares the ELEMENTS inside each list which is true since they reference the same list
print(alist == blist)
# the "is" function compares the id of the lists, which if they refer to the same list, same ids
print(alist is blist)
print("\n")

n1 = 0
n2 = 0
print(n1 is n2, id(n1), id(n2), sep = ", ")

n1 = 255
n2 = 255
print(n1 is n2, id(n1), id(n2), sep = ", ")

n1 = 257
n2 = 257
print(n1 is n2, id(n1), id(n2), sep = ", ")


n1 = -5
n2 = -5
print(n1 is n2, id(n1), id(n2), sep = ", ")

n1 = -1000
n2 = -1000
print(n1 is n2, id(n1), id(n2), sep = ", ")

# python list methods, append, insert, pop, push, sort
# these methods are void calls, and they dont return anything, they just do what the function says

fruit = ["apple", "orange", "banana", "cherry"]
# the "operator" checks true or false whether an object is in a list
# "pear" is not inside the list so it would be false
print("pear" in fruit)

alist = [1, 3, 5]
blist = [2, 4, 6]
print(alist + blist)

# when passing things as parameters are we passing things by value or by references
# but in python we pass everything by reference, even passing things like actual numbers
# below shows that the id are the same

def print_id(num):
    """prints the id of a number"""
    print(id(num))

print(id(2))
print_id(2)

# prints all elements of the list, starting from -1, read from right to left
print([1,2,3,4,5][::-1])
# only reverses surface level of the array
print(list5[::-1])

def make_a_list_out_of_this(phrase):
    """ returns a list made out of phrase """
    # below splits the phrase, which defaults at space " " and returns the individual elements
    # as elements within a list
    return phrase.split()

# what is a vowel sound?
# example beautiful
# beau - ti - ful
# so the vowels are "aeiou"

def does_it_have_3_vowels(word):
    """ checks whether or not the word that is passed in if it has 3 or more vowels return true"""
    vowel_count = 0
    vowels = "aeiou"
    for char in word:
        if char in vowels:
            vowel_count += 1

    if vowel_count > 2:
        return True
    else:
        return False


def check_3_more_vowel(phrase):
    """ this will return a list of words with 3 or more syllables """
    list_of_words = make_a_list_out_of_this(phrase)
    big_word_list = list()
    for index in range(0,len(list_of_words)-1):
        if does_it_have_3_vowels(list_of_words[index]):
            big_word_list.append(list_of_words[index])
    return big_word_list

def main():
    print(make_a_list_out_of_this("holy cow, we can make heavenly beef"))
    print(does_it_have_3_vowels("eeeh"))
    print(check_3_more_vowel("holy cow, we can make heavenly beef"))
    print(check_3_more_vowel("fireboard orange family chocolate banana assonant Africa happiness piano eleven animal Wednesday seventy Melissa chipotle celebrate jessica potato business favorite elephant erica adventure energy history"))

if __name__ == "__main__":
    main()
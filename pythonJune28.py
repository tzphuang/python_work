# ~~ SETS ~~
# sets will add onto a previously defined group of unique variables
# s = {1,3,5,7,9} 
# you can not add in 9 into this set
# what is a set in math?
# it is a unique set of values that can be grouped into a single entity
# common uses in sets are membership testing/removing duplicates/intersection between sets/union between sets
# in python we create sets with {}
# example, s = {1,2,3}
# s = set{iterable}, as long as the items are immutable
# can create sets of anything that is iterable
# Note that {} does not create an empty set, an empty {} is for dictionaries
# to make a empty set you would use its constructor, set()
# sets are unordered, so you cant index/slice/other sequence like behaviors


def unique_word(string_of_words):
    """ This function will return back a list with only 1x of each unique word """
    return_list = []
    list_string_of_words = string_of_words.split()
    for word in list_string_of_words:
        if word not in return_list:
            return_list.append(word)
    return return_list

def unique_set2(phrase):
    return {word for words in phrase.split()}

def main():

    # prints dictionary types
    s = {}
    print(type(s))

    # prints out only unique items
    s = {1,2,2,3,3,4,4}
    print(type(s))
    print(s)

    # single set with string "Python"
    s = {"Python"}
    print(s)

    # function call to unique_word with input string
    # this returns back an array of the string starting with each word showing up at 
    string = "this is a python string that will return back only the unique words in this string"
    print(unique_word(string))

    # another way to make the unique word function is by using sets!
    string = "this is a python string that will return back only the unique words in this string"
    unique_string_set = set(string.split())
    # this will return back a set that is unordered
    print(unique_string_set)

    s1 = {1, 2, 3, 4, 5}
    s2 = {2, 4, 6}
    # prints 1, 3, 5 since s1 is the original set being compared
    print(s1.difference(s2))

# ~~ RANDOM NUMBERS ~~

def random_generation_set(start, end, amount_of_ints):
    import random
    """ this function takes a start and end range, and returns a set of those ints with length
    amount_of_ints """
    if (end+1-start < amount_of_ints):
        return "Length should be less than end+1 - start"
    else:
        s = set()
        while len(s) < amount_of_ints:
            s.add(random.randint(start,end))
    
    return s


def pangram_or_not(phrase):
    """ Checks whether or not phrase, is a pangram or not does not count space """
    #import string
    #s = set(string.ascii_lowercase)
    #return s == (set(phrase.lower()))
    print(set(phrase.lower()))
    return (26 == len(set(phrase.lower())))


def main2():
    import random
    #random.seed(2)
    n1 = random.randint(10,100)
    print(n1)

    group = ["dude1","dude2","dude3","dude4","dude5"]
    print(random.choice(group))

    # this prints out the integers from lowest to highest for some reason
    print(random_generation_set(1,100,2))

    print(pangram_or_not("abcdefghijklmnopqrstuvwxyz"))
    print(pangram_or_not("The quick brown fox jumps over a lazy dog"))


if __name__ == "__main__":
    main()
    main2()
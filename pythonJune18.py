# ~~ Collections ~~
# in float bool are considered simple/primitive data
# but collections such as list and strings are different
# these collections can be treated like their wholes
# or treated as their individual parts
# Strings are sequential collection of characters
# order matters left - right
# strings usually are created with "" or ''
# string = "" is an empty string
# string[] is to access the elements of that string
py = "python"
print(py[0])
# py[0] = "p" ... etc
# you cant add "20" + "20" together to get "40"
# but instead + instead, concatenates the two together
# so "20" + "20" = "2020"
# we say that the math operator +, is overloaded as it does two/more things
twenty = "20"
print(twenty+twenty)
# you can also use the math operator *, it is also overloaded
print(twenty*2)
# len(strings) gets the length, returns it as an integer
print(len(py))
#print(in(py))

# in positive slicing it goes from left to right
# prints "yth"
print("python"[-5:-2])
# in negative slicing it goes from right to left
# starting from right to left slices at -1,
# prints "htyp"
print("python"[-3::-1])
# best way to reverse a string in python, using slicing
print("python"[::-1])
# STRING ITERATION
py = "Python Programming"
for letters in py:
    print(letters)
for index in range(len(py)):
    print(py[index])

# checks if the string has the string "a" and returns a boolean value
# prints true as, programming has an "a"
print("a" in "python programming")
# prints true as there is no "z"
print("z" not in "python programming")
# prints false as "ram" is in the string
print("ram" not in "python programming")

line = "Types that are comprised of smaller pieces are called collection data types. Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts. This ambiguity is useful"
print(len(line))

def reverse_string(rando_string):
    """ this will reverse the passed in string """
    count = 0
    index = -1
    while count < len(rando_string):
        print(rando_string[index], end = "")
        count += 1
        index -= 1
    print("\n")

def easy_reverse(string):
    """ reverses the string input, by starting at index -1 and goes backwards through the string """
    print(string[::-1])

def print_each_char(string):
    """ prints each char of the string on a new line """
    index = 0
    while index < len(string):
        print(string[index]+" ", end = "")
        index += 1
    print("\n")

def word_repeater(string, times):
    """ prints out n number of times of string seperated by ", " """
    print((string + ", ")* times, end = "")
    print("\n")

def linux_to_windows(string):
    """ converts the slash to backslash to make it a windows path """
    # you have to get the string literal by adding an extra backslash
    return string.replace("/","\\")

def isPalindrome(word):
    """ checks if the passed in string is a palindrom """
    return word == word[::-1]

def main():
    reverse_string("python")
    easy_reverse("easy code")
    print_each_char("Python is Awesome")
    print(linux_to_windows("/media/indika/E/Documents/CCSF_PHYC/4AL2018/4ALFriday"))
    word_repeater("crazy", 10)
    print(isPalindrome("tacocat"))


if __name__ == "__main__":
    main()


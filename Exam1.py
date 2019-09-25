print((2**8 - 2*10)//6 -1)
for i in range(2, 11, 2):
    print(i, end = " ")

print()

import random

print(int(101*random.random()))

print(int(100*random.random()))

print(random.randint(0,100))

print(random.randrange(0,100))

print(random.randrange(0,101))


thisset = {"apple", "banana", "cherry"}
#print(thisset[1])
for fruit in thisset:
    print(fruit)

print(len("Return a copy of the string with all occurrences of sub-string old replaced by new. If the optional argument count is given, only the first count occurrences are replaced."))

string_1 = "Python Programming"
print(string_1[7:])

def square_up_to_n(n):
    sum = 0
    for cur_num in range(n+1):
        sum += cur_num**2
    return sum

print(square_up_to_n(4))

def reverse_a_string(string):
    string_1 = string[::-1]
    return string_1

print(reverse_a_string("Yes, please!"))


def return_tuple_list(first_list, second_list):
    return_this_list = [(first_list[index],second_list[index]) for index in range(0,len(first_list))]
    #return_this_list = [tuple(element1, element2) for element1 in first_list, element2 in second_list]
    return return_this_list


list1 = [1, 2, 3] 
list2 = ["a", "b", "c"]
print(return_tuple_list(list1, list2))



# ~~ HOMEWORK 3 ON DICTIONARY ~~

d = {'odd digits': [1,3,5,7,9]}

#d.sort()

#d[odd digits].sort(reverse = True)
d.values()
d.items()
d[2] = 'even digits'



def power_of_2_only(set_input):
    return_set = {num for num in set_input if check_if_power_of_2(num)}
    return return_set

def check_if_power_of_2(num_needing_check):
    power = 0
    power_o_two = 0
    while power_o_two < num_needing_check:
        power_o_two = 2**power
        if power_o_two == num_needing_check:
            return True
        power += 1
    return False

some_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
print(power_of_2_only(some_set1))



# dictionary comprehension example
# {str(i):i for i in [1,2,3,4,5]}

def dict_of_string_words(passed_in_string):
    list_of_string = passed_in_string.split()
    return {word:passed_in_string.index(word) for word in list_of_string}

string1 = "holy guac this is the best dip ever!"
print(string1)
print(dict_of_string_words(string1))

def give_me_dict_power_2_and_3(lower_bound,upper_bound):
    return {num:[num**2,num**3] for num in range(lower_bound,upper_bound+1)}

print(give_me_dict_power_2_and_3(2,9))

# Function keyword arguments: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments (Links to an external site.) 
# Python map() function: https://docs.python.org/3/library/functions.html#map (Links to an external site.) 
# Lambda functions: https://www.python-course.eu/python3_lambda.php (Links to an external site.) 
# Generator expressions: https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions (Links to an external site.)
# Yield statements: http://heather.cs.ucdavis.edu/~matloff/156/PLN/PyIterGen.pdf (Links to an external site.)
# Generators: https://docs.python.org/3/howto/functional.html#generators (Links to an external site.) 
# itertools: https://docs.python.org/3/howto/functional.html#the-itertools-module (Links to an external site.)  
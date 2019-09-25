x = 5
# for all integers beside 0, this will print true -5, 100, 1, 4.9, etc == true
# 0 == false
# for strings of any length besides an empty string == true
# "" == false
if "":
    print(True)
else:
    print(False)

# these are BOOLEANS, since there are no quotes
# this will print 2
# because 1 and 2 are indivually are true, but since 2 is higher, 2 will be the integer that makes 
# this statement true
print(1 and 2)

# recall no quotes means these are booleans
# first part from the left is a 0, which is false, and there is an "and"
# since first item is false, evaluates to 0
print(0 and 2)

# this prints out 1, as 0 maybe false, but 3 is still true
# what is needed to evaluate this expression is 3 
print(0 or 3)

# this will print out 1, as it is the minimum integer to make this expression true
print(1 or 2)

# prints out false because any string that is not empty ("") is true
# and not true == false
print(not "foo")

# while loops how to set up
# while condition:
#   do something

# ~~ in class example to make code~~
# this is the arithmetic progression
# a(n) = a(1) +(n-1)d
# a(50) = 2 + (49)3
# S(n) = n/2(a(1) + a(n))
# s(50) = (50/2)*(2 + (2+(50-1)*3))
# this is the actual summation notation below
print((50/2)*(2 + (2+(50-1)*3))) 
# sigma of a(50) ... a(1)

count = 0
cur_val = 0
sum = 0

while count < 50:
    if count == 0:
        cur_val +=2
        sum += cur_val
        count +=1

    else:
        cur_val +=3
        sum += cur_val
        count +=1

print(sum)


#    def arithmetic_series(start, comm_diff, nth_terms):
#        """ Return the summation of the arithmertic series for nth number""
#        sum = start
#        index = 0
#        while index < nth_terms:
#            sum += comm_diff
#            print(sum)
#            index += 1
#        return sum
#    print(arithmetic_series(2,3,3))


# print all odd numbers between two given numbers without the usage of range

def print_between_two(start, end):
    """ prints between the numbers start and end, only printing the odd integers (inclusive) """
    while start < end:
        if start%2 == 1:
            print(start, end = ", ")
            start += 2
        else:
            print(start, end = ", ")
            start +=1

print_between_two(5,10)
print("\n")
print_between_two(1,100)
print("\n")

# code below used for submittion 
def even_or_not(number):
    """ returns boolean value for whether or not number passed in is even """
    if number%2 == 0:
        return True
    else:
        return False
print(even_or_not(2))

def print_odd_num_in_range(start, end):
    """ prints all odd numbers within range of start(inclusive)- end(inclusive)"""
    while start < end+1:
        if not even_or_not(start):
            print(start, end = ", ")
            start += 2
        else:
            start += 1

print_odd_num_in_range(5,100)

# ~~ NAMING & BINDING ~~   
# in java, c, c++ have a main() function
# python doesnt have this
# we can make a main function in python though

def main():
    print_between_two(5,10)
    print("\n")
    print_between_two(1,100)
    print("\n")
    print(even_or_not(2))
    print_odd_num_in_range(5,100)

# below checks if there is a function with name "main"
# if there is, then call main()
if __name__ == "__main__":
    main()


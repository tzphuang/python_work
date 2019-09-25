# ~~ RECURSION and Python ~~
# an algorithm is recursive if it invokes itself to solve a similar SMALLER problem
# this is usually a function that calls itself
# for recursion, and a recursive call in general
# we have to have a way out of the recursion
# we call this the base case

import timeit
import random

def recursive_factorio(num):
    """ Recrusively calls recursive_factorio to get the factorial of num and returns that value"""
    if num == 1 or num == 0:
        return 1
    else:
        #print("current line is multiplying:", num, "and", num-1)
        return (num * recursive_factorio(num-1))

def iterative_factorio(num):
    """ Iterates through the from 1 to num+1, and multiplies each with sum(=1) and returns sum"""
    if num == 0:
        return 1
    else:
        sum = 1
        for cur_num in range(1,num+1):
            sum *= cur_num
        return sum

def is_it_prime(prime_maybe,divider):
    """Checks if prime_maybe is a prime"""
    if prime_maybe == 1:
        return False

    if divider == 1:
        return True
    else:
        if prime_maybe%divider == 0:
            return False
        else:
            return is_it_prime(prime_maybe, divider-1)

num = 17
print(is_it_prime(num, (num+1)//2))
        
def create_random_list(num):
    return_list = list()
    for num in range(num+1):
        return_list.append(random.uniform(0.0,100.0))
    return return_list

print(create_random_list(100))

def binary_search(search_list,number):
    """impliments the binary search method and searches for the number"""
    if len(search_list) ==1:
        print(search_list)
        return search_list[0] == number
    else:
        if search_list[len(search_list)//2] > number:
            print(search_list)
            return binary_search(search_list[:len(search_list)//2],number) # // = integer division
        else:
            print(search_list)
            return binary_search(search_list[len(search_list)//2:],number)

def fibonacci(num):
    print("entering fibonacci call")
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        print(num-1, "and", num-2)
        return fibonacci(num-1) + fibonacci(num-2)

def main():
    print(recursive_factorio(5))
    print(iterative_factorio(5))
    print(binary_search([1,1,2,3,4,5,6,7,8],8))
    print(fibonacci(5))

if __name__ == "__main__":
    main()
            
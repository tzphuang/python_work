
# coding: utf-8

## Sloutions to coding questions in Week2Day2 in-class quiz

# In[5]:


py1 = "Python "
py2 = "Programming"
print(py1 + py2)
print(py1*5)
print(len(py1*5))
print(len(py1))


# In[6]:


s = "python rocks"
print(s[-3])


# In[7]:


print(len("Types that are comprised of smaller pieces are called collection data types. Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts. This ambiguity is useful"))


# In[80]:


#Q5
def reverse_string1(a_string):
    """prints the reversed a_string"""
    count = len(a_string) - 1 # For accessing from the end
    for i in range(len(a_string)):
        print(a_string[count], end="")
        count -= 1 # Now we go backward  toward zero indexes the loop iterate

def reverse_string2(a_string): # Most recommended solution that you have to do in an interview
    """returns the reversed a_string"""
    return a_string[::-1] # Reverse slice, -1 here means stem size is -1

def reverse_string3(a_string): # Prints None at the end and still don't know why
    """prints the reversed a_string"""
    for i in range((len(a_string)-1), -1, -1): #Except above this also works
        #print(a_string[i])
        #print(i)
        print(a_string[i], end="")

def reverse_string4(a_string): # Prints None at the end and still don't know why
    """prints the reversed a_string"""
    for i in range(-1, -(len(a_string)+1), -1):
        #print(a_string[i])
        #print(i)
        print(a_string[i], end="") #Except above this also works

def return_str_repetition(a_string, how_many):
    """returns a repeated a_string how_many times """
    return (a_string + ", ")*how_many

def is_palindrome1(word):
    """return true if the word is a palindrome"""
    return word == word[::-1]  # Most recommended solution that you have to do in an interview

def is_palindrome2(word):
    """return true if the word is a palindrome"""
    length = len(word)//2
    reverse = len(word)-1
    for item in range(length): # notice we don't have to iterate entire string
        if word[item] != word[reverse]: # We can approch toward center from both ends
            return False
        reverse -= 1
    return True
    
def main():
    reverse_string1("Python")
    print()
    
    print(reverse_string2("Python"))
    print()
    
    print(reverse_string3("Python"))
    print()
    
    
    print(reverse_string4("Python"))
    print()
    
    Linux_path = "/media/indika/E/Documents/CCSF_PHYC/4AL2018/4ALFriday"
    print("The linux path is: ", Linux_path)

    print("The windows path is: ", Linux_path.replace("/", "\\"))

    ## To test out  string mutability un-comment and run below
#     greeting = "Hello, world!"
#     greeting[0] = 'J'            # ERROR!
#     print(greeting)  

    py2 = "Programming"
    print("a" not in py2)
    
    print(return_str_repetition("Python", 10))
    print(is_palindrome1("aaaa"))
    print(is_palindrome2("racecar"))


    
if __name__ == "__main__":
    main()
        
        

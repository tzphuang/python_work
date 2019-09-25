# ~~ HOMEWORK 2 ~~  

# ~~ Q1 ~~
s = "Python rocks"
print(s[7:])
print(s[7:20])
print(s[-5:])
print(s[-5::1])
print(s[-5::])
# ~~ Q2 ~~
py ="pythonic"
print(py[6:5], "t")
print(py[5:6],"o")
print(py[-3],"n")
print(py[5],"y")
print(py[-3:-2],"h")
# ~~ Q3 ~~
#pys = py - "ic"
#print(pys)

# ~~ Q4 ~~
# ~~ Q5 ~~
# ~~ Q6 ~~
# ~~ Q7 ~~
# ~~ Q8 ~~
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[3])

print(numbers[2])

print(numbers[-5])

print(numbers[2:3][0])

print(numbers[-5:-4][0])
# ~~ Q9 ~~
fruits = ["apple", "orange", "banana", "cherry", "mango"]

print("apple" in fruits or "pears" in fruits)

print("apple" in fruits and "pears" in fruits)

print("apple" in fruits)

print("mango" in fruits)

print("pears" in fruits)
# ~~ 10 ~~
l1 = ["python", 1, 500]
l2 = [1, 500, "python"]

print(l1[0] is l2[2]) #returns True

#print(1[1] is l2[0]) #returns True

print(l1[2] is l2[1]) #returns False

print(l1[0] == l2[2]) #returns True

print(l1[1] == l2[0]) #returns True
# ~~ 11 ~~
"""You are given the list, l = [1, 0, 1]. Using only this list, list comprehension and in one line of code obtain the list,

[[1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1]]
Copy paste your one line of code here and change the formatting to preformatted."""

l = [1, 0, 1]
def multiply_array(array):
    list_return = []
    for count in range(1,5):
        list_return.append(array*count)
    print(list_return)

multiply_array(l)

# ~~ 12 ~~
"""You are given a students names and marks as a list of lists as in the form,
[['student name', student marks]]. 
For example, you are given [['student1', 89], ['student2', 96], ['student3', 79]].
Using list comprehensions and one line of code return a sorted (ascending) 
list of only student marks. 
For example in the case you will return [79, 89, 96].

Copy paste your one line of code here and change the formatting to preformatted."""
def sorted_list_grades(array):
    list_grade_only = [current_student[1] for current_student in array]
    #list_grade_only.sort() # modifier function
    list_grade_only = sorted(list_grade_only) # pure function - it returns the sorted list
    return list_grade_only

rndm_student_list = [['student1', 88], ['student2', 96], ['student3', 79]]
print(sorted_list_grades(rndm_student_list))

# using splitters with lists work so do strings (since they are kind of the same anyways)
# print(rndm_student_list[1:])



# ~~ 13 ~~
# read file
# keep count of each new line in file
# return count

# ~~ 14 ~~
# read file first
# read each line indivually and if the first string from index range(0,3) == "def"
# AND the last index, index[-1] is ":" then we add +1 to count
# keep reading until no more lines
# we then return count

# ~~ 15 ~~
# def give_me_subphrase(everything_b4_phrase_delimiter == 1 everything after phrase_delimiter 2, phrase_delimiter, phase):
#   if 1 then we will return everything before the phrase


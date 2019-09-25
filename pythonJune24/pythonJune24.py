# ~~ PYTHON FILES ~~
# files are important because they are not just saved in RAM
# it is saved in secondary memory, where it can be opened later
# opening and closing files, grabbing files, serialization (saving data into hard drive)

# this will default open it to be "read"
# file_varaible1 = open(filename)
# this makes the file you open in "read mode" with the second parameter "r"
# file_variable1 = open(filename, "r")
# this opens a file for writing
# file_variable1 = open(filename, "w")
# this closes a file
# file_varaible1 = close()

# file methods
# read(n)
# returns the next string of "n" characters
# if "n" is omitted the entire file as a single string is returned

# readline(n)
# returns the next line on the file up until the "\n"(newline) character

# some_file = open(somefile.txt, "r")
# for aline in some_file:
#     print(aline)
# some_file.close()

# "With" statements
# this helps with opening and closing a file without writing open, close all the time
# syntax:
# with <create an object that understands context> as <a_name>:
# <do some stuff with that object>
# after its done doing stuff itll close the file

# defaults to read file open("qbdata.txt", "r")
import os
qbfile = open(os.path.expanduser("~/Desktop/python work/pythonJune24/qbdata.txt"))
print(qbfile.readline())
qbfile.close()

with open(os.path.expanduser("~/Desktop/python work/pythonJune24/studentdata")) as data:
    # this for loop takes each line as default storing it in a object called "eachline"
    for eachline in data:
        print(eachline)

        # the split() splits on " " space so, each substring is now stored in an array
        current_line = eachline.split()

        # so if there is an array that has 7 or more in length
        # that means that including the instudents name as an element of the array
        # we have name + 6 scores
        # 7 elements > 6
        # so we choose 6 as our number to compare to
        if len(current_line) > 6:
            print(current_line[0] + " has more than 6 or more scores")

# when opening files they are opened as empty files
# so how do we "edit" files?
# we use appened, and we add on to the existing file

#with open(os.path.expanduser("~/Desktop/python work/pythonJune24/test.txt", "w")) as newfile:
#    newfile.write("Tony H" + "\n")

# created a new file called text.txt
# this is created under user/tony h
with open("test.txt", "w") as newfile:
    newfile.write("Tony H" + "\n")
    newfile.write("Tony h")

with open("test.txt", "w") as newfile:
    newfile.write("Rewritten" + "\n")
    newfile.write("OVERWRITTEN" + "\n")

# this appends anything written to the current existing file, so we dont lose information
with open("test.txt", "a") as newfile:
    newfile.write("something")

def ipchecker(path, ip):
    with open(os.path.expanduser("~/Desktop/python work/pythonJune24/" + path)) as newlist:
        count = 0
        for myline in newlist:
            if ip in myline:
                count += 1
                print(myline)

        print("The number of hits on the ip " + ip + " is " + str(count))

# we can also use the "count" function
# string.count(s, sub[, start[, end]])
# Return the number of (non-overlapping) occurrences of substring sub in string s[start:end].
#  Defaults for start and end and interpretation of negative values are the same as for slices.

ipchecker("IpLog.txt", "66.249.80.0")
ipchecker("IpLog.txt", "123.123.123.123")


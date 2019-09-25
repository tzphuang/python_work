# ~~ files ~~

# imagine having data, pre-made where you had to change it, read it, or use it
# this happens all the time with code
# we have files where we want files and we have to either write something extra
# maybe change something
# or even just use it as data
# here we will use text files as our data files, which are files that are filled with characters
# in python we have to open files before using them
# and then close them once we are done
# here below we have different methods to manipulate files

# open (read)(open(filename, "r")) this opens a file that is passed in as "filename" 
# and this "open" method can only let you read the passed in file

# open (write)(open(filename, "w")) this opens a file that is passed in as "filename"
# and this "open" method lets you write inside "filename"

# close (filevaraible.close()) file in use will now be closed

# ~~ FINDING FILES ON YOUR DISK ~~
# files are saved on your disk in a particular way
# lets say we have a computer
# its a mac
# and we want to access it
# well, first to access it, we have to know where it is
# lets say you wanted this current file "pythonJuly8.py"
# if we look into the extra information we see "Where:"
# and now we see the full path
# "Toph/Users/tonyh/Desktop/python work/pythonJuly8.py" is the entire path
# this is called an absolute file path, and usually this means that
# the path usually ONLY WORKS for the computer its on
# cause what are the freaking chances of having "Toph/Users/tonyh/"
# as the start of the file path?
# also remember file paths are deeper as you go rightward so for example
# in "Toph/Users/tonyh/Desktop/python work/pythonJuly8.py", Toph would encompass the entirety of everything
# but at the right end, "python work" is a folder that HOLDS the python file "pythonJuly8.py"


file_ref = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
file_ref.close()

qb_data = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
for current_line in qb_data: # scans each line up to the "\n" (new line character)
    list_of_stats = current_line.split() # splits each line with delimiter " "(blank space)
    
    # the nice thing about python is that the print line doesnt need to take "+" to concatenate
    # everything together and instead seperates everything by comas where everything will be
    # concatenated together of course without the coma but inbetween where the coma would be
    # a " " (blank space) is inputted instead
    print("QB", list_of_stats[1],",", list_of_stats[0], "had a rating of", list_of_stats[10])
qb_data.close()


# ~~ ALTERNATIVE FILE READING METHODS ~~
# in addition to the "for" loop above
# we also have other methods that python provides which include 
# a single "readline" method: file.readline() that returns the line including the "\n" at the end

# but we also have the "readlines" method: file.readlines() 
# that returns a LIST of all the contents in the file, as a list of strings,
# where each item in the list that can be indexed [0], [1], etc
# is a single line

# we now come to the last type of read line method: file.read()
# this takes the ENTIRE FILE as a single string, everything including spaces
# "\n" newlines, quotes, periods, etc
# and shoves it into a single string

# ~~ USING READLINE() METHOD ~~
qb_data2 = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
my_first_line = qb_data2.readline() # here we store the first line up to "\n" 
                                    # into my_first_line from the file that is stored in qb_data2
print(len(my_first_line))
print(my_first_line)

my_second_line = qb_data2.readline() # here we store the SECOND line up to "\n"
                                     # note that we are storing the second line because
                                     # the first line was already stored and used
                                     # so the file itself qb_data2 doesnt have that data
                                     # and the new "first line" inside the file
                                     # would be the second line
print(len(my_second_line))
print(my_second_line)
qb_data2.close()


# ~~ USING READLINES() METHOD ~~
qb_data3 = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
list_of_lines = qb_data3.readlines()
print(list_of_lines[1]) # prints out Colt McCoy QB CLE  135 222 1576    6   9   60.8%   74.5

first_line_split = list_of_lines[1]
list_of_1st_line = first_line_split.split() # here i take the first line and split it
                                            # as a list and so i can work with indivual
                                            # elements of that list later
print(list_of_1st_line[:2]) # this prints out Colt, McCoy using splitters cause lists can use that
                            # to access its elements
qb_data3.close()

# ~~ USING READ() METHOD ~~
qb_data3 = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
entire_file_string = qb_data3.read()
print(len(entire_file_string))
print(entire_file_string[94:150]) #prints with the ending "\n"
print(entire_file_string[94:149]) #prints without the ending "\n"
qb_data3.close()

# ~~ USING WRITE() METHOD ~~
# file.write(somestring)
# file must be a an opened file that has been specifically opened for writing: file = open(myfile.txt, "w")
# and this will append (somestring) to the end of the file that "file" refers to

# ~~ WRITING TEXT FILES ~~
# with text files we have learned how to read files, but after you read files 
# what do you do with the information?
# well duh, you store it in another file!
# and with that logic, you need to know how to write in another file

# write_file = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/writefile.txt","w")

# remember when we make a new file to write with some things happen
# first we are opening a new file with the name "writefile.txt"
# if this file does not exist, it will make it exist (in the directory specifed)

write_file = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/writefile.txt","w")
write_file.write("cool beans") # here we write cool beans inside the file above called "writefile.txt"
write_file.close()

write_file = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/writefile.txt","w")
# above is an empty file named "writefile.txt" that happened to replace the previous copy above
# this means that the previous copy is now gone and this new file replaced it
# essentially this means that you wiped the writefile.txt of any info
write_file.write("overwritten text") #here we write a new line in the above empty file
write_file.close()

# now lets take both of what we learned and make a program to read from a previous file
# make a new file
# add write onto that file
# and add onto it more, WITHOUT losing previous stored data

read_file = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r")
save_file = open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qb names.txt","w")
for current_line in read_file:
    list_of_current_line = current_line.split()
    save_file.write(list_of_current_line[1] + ", " + list_of_current_line[0] + "\n")
    # the above line appends the current lines's list lastname, first name and new line
    # as a new line in "save_file" this means that nothing is over written
    # and instead it is all saved
read_file.close()
save_file.close()

# why does "while aline" work???
#aline = infile.readline()
#while aline:
#   items = aline.split()
#   dataline = items[1] + "," + items[0]
#   print(dataline)
#   aline = infile.readline()

# ~~ WITH STATEMENTS ~~
# the with statement is quite simple to understand in the context of opening and closing files
# when we open a file we have to close it to let the memory that was being used by said file
# be avaliable again
# but closing files and opening it is a drag to write out time and time again
# so instead there is a automated way of doing it
# with "WITH" statements

# the default way to write "with statments is"
# with <create some object that understands context> as <some names>:
#   do some stuff with the object
#   ... do extra stuff etc
with open("/Users/tonyh/Desktop/python work/filesWorkPythonJuly8/qbdata.txt","r") as qb_data4:
    qb_data4.readline() # this eats the first line in the file and since its not assigned to anything
                        # its just passed over
    print(qb_data4.readline()) # then we get to the second line where the actual first quarter back
                               # is named and we print out the whole line
# and now that its done we are finished and the file is automatically closed due to the "with" statement

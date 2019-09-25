def scan_my_file_for_phrase(file):
    import os
    with open(os.path.expanduser("~/Desktop/python work/"+file)) as data:
        """This function takes in a file and then scans through each line looking for each line
        that begins with "def " and ends with ":" and stores that line in a list
        The length of that list is the amount of function definitions are in that file """
        current_line_index = 1
        list_of_lines = []
        for eachline in data:
            # (":" == eachline[-1] or ":" == eachline[-2])
            # the reason why this code is here is because it scans the last TWO characters of the string
            # for whether they are ":" because the invisible return key counts as a character
            if ("def " == eachline[0:4]) and (":" == eachline[-1] or (":" == eachline[-2] and "\n" == eachline[-1])):
                list_of_lines.append(current_line_index)
            current_line_index += 1
        return list_of_lines

def main():
    print(scan_my_file_for_phrase("ihaveadreamspeech.txt"))
    print(len(scan_my_file_for_phrase("ihaveadreamspeech.txt")))

if __name__ == "__main__":
    main()
def scan_my_file_for_phrase(file,phrase):
    import os
    #with open(os.path.expanduser("~/Desktop/python work/pythonJune24/studentdata")) as data:
    with open(os.path.expanduser("~/Desktop/python work/"+file)) as data:
        """ this program takes in a file and returns each line inside that file that has "phrase" in it """

        # this for loop takes each line as default storing it in a object called "eachline"
        current_line_index = 1
        list_of_lines = []
        for eachline in data:
            #print(eachline)
            if phrase in eachline:
                list_of_lines.append(current_line_index)
            current_line_index += 1
        #list_of_lines = [number for current_line in data if "Negro" in current_line]
        return list_of_lines

def main():
    print(scan_my_file_for_phrase("ihaveadreamspeech.txt","Negro"))

if __name__ == "__main__":
    main()
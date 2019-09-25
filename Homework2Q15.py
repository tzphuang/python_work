def phrase_delimiter(phrase,delimiter,before):
    """This function takes in a phrase, and breaks that phrase into a before and after
    in regards to a delimiter that is also passed in, if "before" is true, than we take the
    first half before the delimiter, if before is false, we take the second half """
    if before:
        return_string = phrase[:(phrase.find(delimiter))]
    else:
        return_string = phrase[(phrase.find(delimiter)+len(delimiter)):]

    return return_string

def main():
    print(phrase_delimiter("thuang54@mail.ccsf.edu","@",False))
    print(phrase_delimiter("thuang54@mail.ccsf.edu","@",True))

if __name__ == "__main__":
    main()

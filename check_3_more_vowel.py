def make_a_list_out_of_this(phrase):
    """ returns a list made out of phrase """
    # below splits the phrase, which defaults at space " " and returns the individual elements
    # as elements within a list
    return phrase.split()

# what is a vowel sound?
# example beautiful
# beau - ti - ful
# so the vowels are "aeiou"

def does_it_have_3_vowels(word):
    """ checks whether or not the word that is passed in if it has 3 or more vowels return true"""
    vowel_count = 0
    vowels = "aeiou"
    for char in word:
        if char in vowels:
            vowel_count += 1

    if vowel_count > 2:
        return True
    else:
        return False


def check_3_more_vowel(phrase):
    """ this will return a list of words with 3 or more syllables """
    list_of_words = make_a_list_out_of_this(phrase)
    big_word_list = list()
    for index in range(0,len(list_of_words)-1):
        if does_it_have_3_vowels(list_of_words[index]):
            big_word_list.append(list_of_words[index])
    return big_word_list

def main():
    print(make_a_list_out_of_this("holy cow, we can make heavenly beef"))
    print(does_it_have_3_vowels("eeeh"))
    print(check_3_more_vowel("holy cow, we can make heavenly beef"))

if __name__ == "__main__":
    main()
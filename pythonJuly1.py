# ~~ Dictionaries ~~

def sort_student_id(array_names,array_ids):
    """ prints out each unique id with associated student in a single line starting with the
    first numerical value of the id first """
    sorted_list_ids = array_ids.copy()
    sorted_list_ids.sort()
    for current_id in sorted_list_ids:
        print(array_names[array_ids.index(current_id)],current_id)


# array_names = list("joe","bob","ham","mat")
# array_ids = list(111,7,2020,1982)
array_names = ["joe","bob","ham","mat"]
array_ids = [111,7,2020,1982]
sort_student_id(array_names,array_ids)

# dictionaries are not sequential
# it can be considered a map, an unordered associative collection
# where you can map keys, to values
# in a real life example we have the keys (words), and they are mapped 1 to 1 to values (definitions)
# we create dictionaries with {} (this is also the way to make sets)
# if we want associative pairs it would be like
# dictionary_name = {key1:value1, key2:value2}
dictionary_1 = {"name":"Tony","school":"ccsf"}
# keys are immutable but values can be mutable, where you can changes what key is associated to what value
inventory = {'apples': 430, 'bananas': 312, 'bananas': 3142}
print(inventory)
# this will out all the keys
for key in inventory:
    print(key)

for keys, values in inventory.items():
    print(keys, values)

# keys act as the index or accessor in this case
# so to get the value for bananas
# we type in inventory['bananas']
print(inventory['bananas'])
# the quotes '' or "" dont exactly matter as long as theyre there
print(inventory["apples"])

# also remember that dictionaries are also mutable
# you can create aliases and then change the values
d1 = {"name": "indika", "id": 1234}
d2 = d1
d2["name"] = "John"
print(d1)

# you can also copy the dictionaries as they are objects that refer to memory
d1 = {"name": "indika", "id": 1234}
d2 = d1.copy()
d2["name"] = "John"
print(d1)
print(d2)

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
# these keys, are now a "dictionary view object"  where they are iterable, and you cna
# manipulate the objects in that view object and put them into a list
print(keys)
print(list(keys))

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
values = dishes.values()
print(list(values))

def is_Pangram(phrase):
    """ checks if phrase is a pangram, using dictionaries """
    if len(phrase) < 27:
        print("phrase is not a pangram because there are less than 27 characters")
        return False
    phrase = phrase.lower()
    dictionary = {}
    for letters in phrase:
        # this sets every UNIQUE key to have a value of an empty string
        dictionary[letters] = ""
    return len(dictionary) == 27

print(is_Pangram("The quick brown fox jumps over a lazy dog"))
print(is_Pangram("The quick brown fox jumps over a laaaaaaaaaaay dog"))

def pangram_alphabet_counter(phrase):
    """ checks if phrase is a pangram, using dictionaries while keeping count for each letter
    in the phrase that was passed in """
    if len(phrase) < 27:
        print("\"" + phrase + "\" is not a pangram because there are less than 27 characters")
        return False

    phrase = phrase.lower()
    dictionary = {}
    for letters in phrase:
        # this sets every UNIQUE key to have a value of one
        if letters not in list(dictionary.keys()):
            dictionary[letters] = 1
        else:
            dictionary[letters] += 1
    if len(dictionary) == 27:
        print("The phrase \"" + phrase + "\" is a pangram")
        return dictionary
    else:
        print("The phrase \"" + phrase + "\" is not a pangram, RIP")
    
print(pangram_alphabet_counter("notlongenough"))
print(pangram_alphabet_counter("The quick brown fox jumps over a lazy dog"))
print(pangram_alphabet_counter("The quick brown fox jumps over a laaaaaaaaaay dog"))
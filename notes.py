While Loops
    count = 0
    while count < 100:
        print(count)
        count = count + 1
For Loops
    for count in range(100):
        print(count)

Files: Files can be treated as lists of lines we can loop through.
    # "open" the file
    # getting a reference to it
    file = open('myfile.txt') #relative path

    for line in file:
        print(line)

How many words?
    file = open('words.txt')

    count = 0
    for line in file:
        count = count + 1

    print(count, "words")

    file = open('sonnet_xviii.txt')

    count = 0
    for line in file:
        words = line.split(' ') #space delimiter
        for word in words: # NESTED for loop
            count = count + 1

    print(count, "words") <-- prints 120 words

    import re #for regex
    file = open('sonnet_xviii.txt')

    count = 0
    for line in file:
        # split on regex (not word or ' chars)
        words = re.split("[^\w']+", line) <-- not inside group, with "'", repeated once or more
        for word in words:
          if word != '':
            #print(word)
            count = count + 1

    print(count, "words") <-- prints 115 words (use regex to increase specificity)

    import sys <-- gives access to "argv" (command line arguments)

Average letters per line?
    file = open('words_huge.txt')

    total_ltr = 0
    count = 0
    for line in file:
        total_ltr = total_ltr + len(line)
        count = count + 1

    avg_len = total_ltr/count

    print("Average word length:", avg_len)

Does it contain a word? ("Linear Search" - look at every single thing, one anfter another)
    file = open('words.txt')

    target = input("Word to find: ")

    found = False
    for line in file:
        if line == target:
            found = True
        # NO ELSE

    if found:
        print(target + " is in the list!")

    # would find dogma & dog, use regex
    file = open('book.txt')
    target = input("Word to find: ")

    found = False
    for line in file:
        if target in line:
            found = True

    if found:
        print(target + " is in the list!")

Longest Word? ("king of the hill search")
    file = open('words.txt')

    largest = "" <--initialize king
    for line in file:
        if len(line) > len(largest): <-- compare to king
            largest = line ,-- save new king

    print(largest + " is the largest!")

All words shorter than n? "Exclusion Search": might need to reverse logic (is there one word that's not small'?)
    file = open('words.txt')
    max_length = int(input("Max word length? "))

    all_short = True
    for line in file:
        if len(line) > max_length:
            all_short = False
            break #can leave early (stop looping, quit, ctrl c) --> could be "continue"; rather than using break, might want to change conditions under which you are looping - mb should b using while loop instead of a for loop and then u should change your sentinel conditions

    if all_short:
        print("All words short")
    else:
        print("A word was long")

Lists: A mutable, ordered sequence of values. (comma-separated in square brackets)
    names = ["John", "Paul", "George", "Ringo"]
    letters = ["a", "b", "c"]
    numbers = [1, 2, 3]
    things = ["raindrops", 2, True, [5, 9, 8]]
    empty = []

Accessing Lists: We access individual items in a list using square brackets (specify the "room number")
    names = ["John", "Paul", "George", "Ringo"]

    print(names[0]) # => "John"
    print(names[1]) # => "Paul"
    print(names[2]) # => "George"
    print(names[3]) # => "Ringo"
    print(names[4]) # => IndexError!

List Indices: Index indicates a "room number", and can itself be a variable.
    letters = ["a", "b", "c", "d", "e"]

    x = 2
    print(names[x]) # => "c"
    x = 1
    print(names[x]) # => "b"

Index Bounds: The indices of a go from 0 to the length of the list - 1.
    names = ["John", "Paul", "George", "Ringo"]

    #length of the list
    len(names) #=> 4

    names[ len(names) ] # out of bounds
    names[ len(names)-1 ] # in bounds

List Entries: The list[index] itself is a variable!
    #change from this...

    print(letter0) # => "a"
    print(letter1) # => "b"
    print(letter2) # => "c"
    print(letter3) # => "d"

    #                   ...to this

    print(letters[0]) # => "a"
    print(letters[1]) # => "b"
    print(letters[2]) # => "c"
    print(letters[3]) # => "d"

Changing Lists: The list[index] itself is a variable. Which means we can assign values to them!
    values = [1, 2, 3, 4]

    values[0] = "a"
    values[1] = "b" # 1 is index, not value!
    values[2] = "c"
    values[3] = "d"

    print(values) #=> ['a', 'b', 'c', 'd']

    values[4] = "f" #=> IndexError!

More Indices:
    values = ['a', 'b', 'c', 'd', 'e', 'f']

    values[5] #=> 'f'

    # negatives count from end!
    # (alias for len(list) + var)
    values[-1] #=> 'f'
    values[-2] #=> 'e'

    ## colons "slice" a range of entries ##

    # indices 1 through 3 (non-inclusive)
    values[1:3] #=> ['b', 'c']

    # indices 3 to the end (inclusive)
    values[3:] #=> ['d', 'e', 'f']

    # indices up to 3 (non-inclusive)
    values[:3] #=> ['a', 'b', 'c']

    # indices 2 to (2 from end) (non-inclusive)
    values[2:-2] #=> ['c', 'd']
    values[-1] --> last item in list
    values[len(values)-1] --> last item in list

List Functions: 
    # combine lists
    ['a','b'] + [1,2] #=> ['a','b',1,2]
    #repeat lists
    [1,2]*3 #=> [1, 2, 1, 2, 1, 2] 

    #add value to end of list
    s.append('x') #add 'a' at end
    trying to add multiple entries via append will not work

    #add value in middle of list
    s.insert(2, 'y') #put 'y' at index 2

    #remove from end of list
    s.pop()

    #remove from middle
    s.pop(2) #remove item at index 2

    #remove specific value
    s.remove('c') #remove the first 'c'

    #remove everything
    s.clear()

List functions usually mutate the list and return None. (lists will change)

String functions usually return a different String. (strings are immutable)

Lists and Loops:
    values = ['a','b','c','d']

    for item in values:
        print(values)

    for i in range(len(values)):
        values[i] = values[i].upper()
                  ^a "mapping" (mapping from lowercase versions to uppercase versions)
                  i is for index

Object References
    a = "banana" #a labels string "banana"
    b = "banana" #b labels string "banana"

    a is b #=> True
    #both refer to the same string

    a = [1,2,3] #a labels list [1,2,3]
    b = [1,2,3] #b labels list [1,2,3]

    a == b #=> True; have same values
    a is b #=> False
    #both lists have same contents,
    #but are DIFFERENT OBJECTS (things)
    "Lists can be equivalent without being identical"
    c = a #c labels the value of a
    a is c #=> True
    #both variables refer to same object

Lists and Functions:
    def delete_first(a_list):
        a_list = a_list[1:] #make local variable only!

    letters = ['a','b','c']
    delete_first(letters)
    print(letters) #=> ['a', 'b', 'c']

    def delete_first(a_list):
        a_list.pop(0) #modifies the list

    letters = ['a','b','c']
    delete_first(letters)
    print(letters) #=> ['b', 'c']

    def negate(a_list):
        for item in a_list:
            item = -1*item #make local variable only!

    numbers = [1,2,3]
    negate(numbers)
    print(numbers) #=> [1, 2, 3]

    def negate(a_list):
        for i in range(len(a_list)):
            a_list[i] = -1* a_list[i] #reassign value

    numbers = [1,2,3]
    negate(numbers)
    print(numbers) #=> [-1, -2, -3]

Nested Lists: Lists can contain other lists (called a 2D-list). The "outer" list is still a variable!
    # a list of lists
    mult_table = [ [0,0,0,0,0], 
               [0,1,2,3,4], 
               [0,2,4,6,8], 
               [0,3,6,9,12], 
               [0,4,8,12,16] ]

    mult_table[1]     #=> [0,1,2,3,4] (a list)

    first_list = mult_table[1]

    first_list[2]     #=> 2 (a # in that list)

    mult_table[1][2]  #=> 2 (a # in a list in a list)

"questions on" +
['lists','indices','references']
+"?"

Dictionaries: A unordered set of "key & value" pairs.
    Similar to a real world dictionary: you have the word (the key) and the definition (the value). Use the key to look up the value.
    Provides a mapping from keys to values

    ages = {'alice':42, 'bob':35, 'charles':13}
    extensions = {'joel':1622, 'ischool':9937}
    num_words = {1:'one', 2:'two', 3:'three'}
    things = {'num':12, 'dog':'woof', 'list':[1,2,3]}
    empty = {}

Accessing Dicts: We access individual values in a dict using square brackets (specify the key as the "room number")
    ages = {'alice':42, 'bob':35, 'charles':13}

    print(ages['alice']) # => 42
    print(ages['bob']) # => 35 <--"lookups"
    print(ages['charles']) # => 13

    print(names[42]) # => KeyError!
    print(names['fred']) # => KeyError!

    #get() function returns value OR default
    names.get('alice', 0) # => 42, the value
    names.get('fred', 0) # => 0, the default

Changing Dicts: The dict[key] itself is a variable. Assigning a value to a new key will add that key to the dictionary.
    "dicts are unordered"

    d = {'a':1, 'b':2, 'c':3}

    d['a'] = 5
    print(d) #=> {'c': 3, 'a': 5, 'b': 2}

    d['x'] = 12 #assigns value to NEW key
    print(d) #=> {'c': 3, 'x': 12, 'a': 5, 'b': 2}

How many of each letter?
    text = "Mississippi"

    #number of letters
    a = 0
    b = 0
    c = 0
    #...

    for letter in text:
        if letter == 'a':
            a += 1 #shortcut for a = a + 1
        if letter == 'b':
            b += 1
        #...
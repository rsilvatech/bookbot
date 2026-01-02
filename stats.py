# List of functions for analysing text

def count_book_words(path_to_file):
    # Turns a book.txt file into a list of strings (book_words) 
    with open(path_to_file) as book:
        book_as_string = book.read()
    book_words = book_as_string.split()
    
    # Counts the amount of words inside book_words
    num_words = 0
    for word in range(0, len(book_words)):
        num_words += 1

    return num_words

def count_book_characters(path_to_file):
    # Turns a book.txt file into a big string (book_as_string) 
    with open(path_to_file) as book:
        book_as_string = book.read()

    #counts the amount of characters inside book_as_string an make a pair of character-->quantity inside the num_each_character dictionary
    character_count = {}
    for character in book_as_string:
        character = character.lower()
        if (character in character_count):
            character_count[character] += 1
        else:
            character_count[character] = 1
    
    return character_count

def sort_on(items):
    return items["num"]

def sort_character_count(path_to_file):
    character_count = count_book_characters(path_to_file)
    each_character_num = []
    for character in character_count:
        if (character.isalpha() == True): 
            name_num_pair = {}
            name = character
            num = character_count[character]
            name_num_pair["name"] = name
            name_num_pair["num"] = num
            each_character_num.append(name_num_pair)
            each_character_num.sort(reverse=True, key=sort_on)
        else:
            pass
    return each_character_num     

    

               

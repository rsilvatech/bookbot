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
    num_each_character = {}
    for character in book_as_string:
        character = character.lower()
        if (character in num_each_character):
            num_each_character[character] += 1
        else:
            num_each_character[character] = 1
    
    return num_each_character
        

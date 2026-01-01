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


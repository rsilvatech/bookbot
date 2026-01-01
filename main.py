#bookbot - Programa em Python que analisa arquivos de texto e imprime um relatório estatístico do uso de palavras e caracteres encontrados neles.

def get_book_text(path_to_file):
    with open(path_to_file) as book:
        return book.read()

book_as_string = get_book_text('./books/frankenstein.txt')

def count_book_words(book_as_string):
    book_words = book_as_string.split()
    num_words_f = 0
    for word in range(0, len(book_words)):
        num_words_f += 1
    return num_words_f

num_words = count_book_words(book_as_string)

def main():
    print(f"Found {num_words} total words")
    

main()

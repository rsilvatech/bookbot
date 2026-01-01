#bookbot - Programa em Python que analisa arquivos de texto e imprime um relatório estatístico do uso de palavras e caracteres encontrados neles.

from stats import count_book_words, count_book_characters

path_to_file = './books/frankenstein.txt'

def main():
    print(f"Found {count_book_words(path_to_file)} total words")
    print(count_book_characters(path_to_file))
    
main()

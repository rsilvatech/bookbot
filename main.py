#bookbot - Programa em Python que analisa arquivos de texto e imprime um relatório estatístico do uso de palavras e caracteres encontrados neles.

import stats, sys

path_to_file = "./books/frankenstein.txt"

sorted_character_dict = stats.sort_character_count(path_to_file)

def main():
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {stats.count_book_words(path_to_file)} total words")
    print("--------- Character Count -------")
    for pair in sorted_character_dict:
        print(f"{pair['name']}: {pair['num']}")
    print("============= END ===============")

main()


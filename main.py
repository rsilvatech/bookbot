#bookbot - Programa em Python que analisa arquivos de texto e imprime um relatório estatístico do uso de palavras e caracteres encontrados neles.

import stats, sys

#catchs input from the terminal to set the path_to_file variable (path/to/file/book.txt)
if ((len(sys.argv)==2) == True):
    path_to_file = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#catches the result of sort_character_count into a variable
#its a list of dictionaries containing a pair of "name" and "num"
sorted_character_dict = stats.sort_character_count(path_to_file)

#calls the functions and outputs the result on the terminal
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


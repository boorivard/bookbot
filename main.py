import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_dictionary

#function that takes a file and converts the content of that file to a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#function that prints the results in the desired format
def print_results(num_words, num_chars, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def main():
    #checks to see if number of arguments is equal to two
    #if not, print a usage message and exit with code 1
    #if it does, set book_path equal to the provided filepath
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #gets book text from book path
    book_text = get_book_text(book_path)
    #get number of words in the text
    num_words = get_num_words(book_text)
    #get the number of each character in the text
    num_chars = get_num_char(book_text)
    #sort the dictionaries by number of times the character appears
    num_chars = sort_dictionary(num_chars)

    #print results
    print_results(num_words, num_chars, book_path)

main()

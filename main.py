from stats import get_num_words
from stats import get_num_char
from stats import sort_dictionary

#function that takes a file and converts the content of that file to a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_results(num_words, num_chars):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in num_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


def main():
    #gets frankenstein text from dir books
    book_text = get_book_text("books/frankenstein.txt")
    #get number of words in the text
    num_words = get_num_words(book_text)
    #get the number of each character in the text
    num_chars = get_num_char(book_text)
    num_chars = sort_dictionary(num_chars)

    #print results
    print_results(num_words, num_chars)

main()

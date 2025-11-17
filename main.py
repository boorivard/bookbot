from stats import get_num_words
from stats import get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    num_chars = get_num_char(book_text)
    print(f"Found {num_words} total words")
    print(num_chars)

main()

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_text):
    return

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()

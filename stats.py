def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_char(book_text):
    num_char = {}
    for c in book_text:
        c = c.lower()
        if c in num_char:
            num_char[c] += 1
        else:
            num_char[c] = 1
    return num_char
#function takes the string of text and returns the number of words in the text
def get_num_words(book_text):
    #get a list of all the words using the split function
    words = book_text.split()
    #returns the length of the list
    return len(words)

#function takes the string of text and returns a dict of all the characters
#and their number of appearences in the text
def get_num_char(book_text):
    #create empty dict
    num_char = {}

    #for each char
    for c in book_text:
        #convert char to lower if necessary 
        c = c.lower()
        #if the char is already in our dict, add 1; else initialize it with a count of 1
        if c in num_char:
            num_char[c] += 1
        else:
            num_char[c] = 1
    #return the dict
    return num_char

def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    sorted_list = []
    for char in dict:
        new_dict = {"char": char, "num": dict[char]}
        sorted_list.append(new_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

    

        


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

#function returns the value of key num for the dictionaries
def sort_on(items):
    return items["num"]

#function returns a list of the dictionaries sorted by most to least in the num key
def sort_dictionary(dict):
    #create empty list
    sorted_list = []
    #for each item in the dictionary
    for char in dict:
        #create a new dictionary with 2 key value pairs:
        #char: 'char' and num: num_of_char
        new_dict = {"char": char, "num": dict[char]}
        #add the new dictionary to the list
        sorted_list.append(new_dict)
    
    #sort the list in reverse by num
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

    

        


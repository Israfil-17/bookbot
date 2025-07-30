def get_book_text(path_to_file):
    with open(path_to_file) as text:
        file_content = text.read()
        return file_content

def word_num():
    words = get_book_text("books/frankenstein.txt").split()
    word_count = len(words)
    print(f"{word_count} words found in the document")

def ch_count():
    words = get_book_text("books/frankenstein.txt")
    dict = {}
    for c in words:
        lower = c.lower()
        if lower not in dict:
            dict[lower] = 1
        else:
            dict[lower] += 1
        
    print(dict)



#Loop through each character in the text string
#Convert each character to lowercase using .lower()
#For each character, either:
#Add it to the dictionary with a count of 1 (if it's the first time you've seen it)
#Increment its count by 1 (if you've seen it before)
    

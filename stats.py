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
    return dict

def sort_on(dict):
    return dict["num"]

def list_dicts():
    dict_list = []
    for 

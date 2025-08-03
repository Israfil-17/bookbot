def get_book_text(path_to_file):
    with open(path_to_file) as text:
        file_content = text.read()
        return file_content

def word_num():
    words = get_book_text("books/frankenstein.txt").split()
    word_count = len(words)
    print(f"Found {word_count} total words")
    return print(f"Found {word_count} total words")
    

def ch_count():
    words = get_book_text("books/frankenstein.txt")
    char_dict = {}
    for c in words:
        lower = c.lower()
        if lower not in char_dict:
            char_dict[lower] = 1
        else:
            char_dict[lower] += 1
    dict_list = []
    for item in char_dict:
        rep = char_dict[item]
        new_dict = {}
        new_dict["char"] = item
        new_dict["num"] = rep
        dict_list.append(new_dict)
        def sort_on(item):
            return item["num"]

    dict_list.sort(reverse=True, key=sort_on)
    
    result = []
    for value in range(0, len(dict_list)):
        char = dict_list[value]["char"]
        num = dict_list[value]["num"]
        if char.isalpha():
            result.append(f"{char}: {num}")
            print(f"{char}: {num}")
    
    return result


    



    


        


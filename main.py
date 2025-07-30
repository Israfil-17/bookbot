def get_book_text(path_to_file):
    with open(path_to_file) as text:
        file_content = text.read()
        return file_content

def main():
    words = get_book_text("books/frankenstein.txt").split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
    


main()
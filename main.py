import sys


def main():
    try:
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        from stats import word_num
        word_num(path_to_file)

        print("--------- Character Count -------")
        from stats import ch_count
        ch_count(path_to_file)
        print("============= END ===============")
    except IndexError as e:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)


main()
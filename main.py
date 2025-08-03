def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    from stats import word_num
    word_num()

    print("--------- Character Count -------")
    from stats import ch_count
    ch_count()
    
    
    print("============= END ===============")



main()
import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text( filepath ):
    with open(filepath) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    filepath = sys.argv[1]
    print(f"Analyzing book found at {filepath}...")
    book_text = get_book_text(filepath)
    word_count = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_char_count(char_count)

    print("----------- Word Count ----------")
    print(f'Found {word_count} total words.')
    print("--------- Character Count -------")
    for char, count in sorted_char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


main()
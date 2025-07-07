from stats import count_words, char_counts, char_dics
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def sort_on(items):
    #print(items["num"])
    return items["num"]

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    print("Found 75767 total words")
    #print(char_counts(get_book_text("books/frankenstein.txt")))
    char_list = char_dics(char_counts(get_book_text(sys.argv[1])))
    #print("char_list", char_list)
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(item["char"]+":", item["num"])

if __name__ == "__main__":
    main()

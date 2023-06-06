
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    counts = {}
    words = text.split()
    for word in words:
        for letter in word.lower():
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
    return counts


def print_report(bookname, wordcount, lettercount):
    print(f"--- Begin report of {bookname} ---")
    print(f"{wordcount} words found in the document")
    print("")


    letter_list = list(lettercount.items())

    letter_list.sort(key = lambda x: x[1], reverse = True)

    for letter in letter_list:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")


bookname = "books/frankenstein.txt"


with open(bookname) as f:
    file_contents = f.read()

    print_report(bookname, count_words(file_contents), count_letters(file_contents))

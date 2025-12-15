def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    char_counts = letter_count(text)
    print(char_counts)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def letter_count(text):
    lower_text = text.lower()
    counts = {}
    for char in lower_text:
        if char in counts:
            counts[char] = counts[char] + 1
        else:
            counts[char] = 1
    return counts

def letter_sort(letter_count):
    letter_count.sort()
    print(f "{char}: {counts}")
    return

main()

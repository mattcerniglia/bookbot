def get_book_text(path):
  with open(path) as f:
    path = f.read()
    return path
def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  print(f"Found {num_words} total words")
  
main()

def get_num_words(text):
  words = text .split()
  return len(words)

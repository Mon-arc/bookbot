
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_words(text)
    chars_freq = get_chars(text)

    print_report(book_path, count, chars_freq)


def get_words(book_text):
  words = book_text.split()
  count = len(words)
  return count

def get_chars(text):
  characters = {}
  new_text = text.lower()

  for c in new_text:
    if c in characters:
      characters[c] += 1
    else:
      characters[c] = 1
  return characters

def get_book_text(path):
  with open(path)as f:
    file_contents = f.read()
  return file_contents

def print_report(path, word_count, characters):
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document\n")
  chars_to_remove = [
    ' ', "'", ',', '(', ')', '\n', '.',
     '-', ':', '1', '2', '3', '4', '5',
     '6', '7', '8', '9', '0', '[', ']',
     '#', '*', '?', ';', '!', '"', '_',
     '/', '%', '@', '$']
  filtered_chars = []

  for c in characters:
    if c not in chars_to_remove:
      print(f"the '{c}' charcter was found {characters[c]} times")
  print("--- End of Report ---")
  

main()
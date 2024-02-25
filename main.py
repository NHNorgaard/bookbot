def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_dict = letter_count(text)
    report = char_report(letters_dict)

    print(f"Counted report of {book_path}")
    print(f"{num_words} total words found in the document")

    for item in report:
        print(f"The {item["letter"]} was found {item["num"]} times")
    print("End of report")
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    l_count = {}
    alphabetic_text = ""
    for char in text.lower():
        if char.isalpha():
            alphabetic_text += char
    for letter in alphabetic_text:
        if letter not in l_count:
            l_count[letter] = 1
        else:
            l_count[letter] += 1
    return l_count

def char_report(letters_dict):
    for_sorting =[]
    for letter, count in letters_dict.items():
        new_dict = {"letter": letter, "num": count}
        for_sorting.append(new_dict)
    def sort_on(letters_dict):
        return letters_dict["num"]
    for_sorting.sort(reverse=True, key=sort_on)
    return for_sorting



main()
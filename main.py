def main():
    file_contents = read_file()
    lower_cased = to_lower(file_contents)
    chars_dict = unique_letter_count(lower_cased)
    chars_list = to_list(chars_dict)
    word_count = count_words(file_contents)
    for item in chars_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

def read_file():
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_words(file_contents):
    split_file = file_contents.split()
    return len(split_file)

def to_lower(file_contents):
    return file_contents.lower()

def unique_letter_count(lower_cased):
    chars = {}
    for letter in lower_cased:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1   
    return chars    

def to_list(chars_dict):
    temp_list = []
    for ch in chars_dict:
        temp_list.append({"char": ch, "num": chars_dict[ch]})
    temp_list.sort(reverse=True, key=sort_on)
    return temp_list


def sort_on(d):
    return d["num"]

main()

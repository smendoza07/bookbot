def main():
    file_contents = read_file()
    lower_cased = to_lower(file_contents)
    chars_dict = unique_letter_count(lower_cased)
    chars_list = []
    chars_list = to_list(chars_dict)
    word_count = count_words(file_contents)
    to_list(chars_dict)
    print(chars_list)

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
    for key, val in chars_dict.items():
        if not isinstance(val, list):
            val = [val]  # Convert non-list values to a list
        temp_list.append([key] + val)
    return temp_list


# def sort_on(dict):
#     return dic[]

main()

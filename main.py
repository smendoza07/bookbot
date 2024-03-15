import os

def main():
    choice = menu()
    filename = select_book()
    filepath = os.path.join("books", filename)
    file_contents = read_file(filepath)
    lower_cased = to_lower(file_contents)
    chars_dict = unique_letter_count(lower_cased)
    chars_list = to_list(chars_dict)
    word_count = count_words(file_contents)
    if choice == '1':
        print_word_count(f'There are a total of {word_count} words in the text')
    else:
        print_letter_frequency(chars_list)

def select_book():
    print("Select a text file:")
    file_list = os.listdir("books")
    for i, filename in enumerate(file_list, start=1):
        print(f"{i}. {filename}")
    choice = input("\nEnter the number corresponding to your choice: ")
    try:
        choice_index = int(choice) - 1
        selected_file = file_list[choice_index]
        return selected_file
    except (ValueError, IndexError):
        print("\nInvalid choice. Please try again.\n")
        return select_book()

def print_word_count(word_count):
    print(word_count)

def print_letter_frequency(chars_list):
    for item in chars_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

def menu():
    print("1.) Total word count.\n")
    print("2.) Letter frequency.\n")
    choice = input('Select one of the choices from above: ')
    if choice != '1' and choice != '2':
        print(f'\n{choice} is invalid, please try again\n')
        menu()
    return choice

def read_file(filepath):
    with open(filepath) as f:
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

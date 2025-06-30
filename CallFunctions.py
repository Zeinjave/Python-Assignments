# Define your functions here.

def print_menu():
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")
    print()

def get_num_of_non_WS_characters(text):
    return sum(1 for char in text if not char.isspace())

def get_num_of_words(text):
    words = text.split()
    return len(words)

def fix_capitalization(text):
    capitalize_next = True
    new_text = ""
    cap_count = 0

    for char in text:
        if capitalize_next and char.isalpha():
            if char.islower():
                new_text += char.upper()
                cap_count += 1
            else:
                new_text += char
            capitalize_next = False
        else:
            new_text += char
            if char in ".!?":
                capitalize_next = True
            elif char not in " \n\t":
                capitalize_next = False

    return new_text, cap_count

def replace_punctuation(text, exclamation_count=0, semicolon_count=0):
    exclamation_count = text.count('!')
    semicolon_count = text.count(';')
    new_text = text.replace('!', '.').replace(';', ',')
    print("Punctuation replaced")
    print(f"exclamation_count: {exclamation_count}")
    print(f"semicolon_count: {semicolon_count}")
    return new_text

def shorten_space(text):
    import re
    return re.sub(r'\s{2,}', ' ', text)

def execute_menu(choice, text):
    if choice == 'c':
        count = get_num_of_non_WS_characters(text)
        print(f"Number of non-whitespace characters: {count}")
    elif choice == 'w':
        count = get_num_of_words(text)
        print(f"Number of words: {count}")
    elif choice == 'f':
        text, cap_count = fix_capitalization(text)
        print(f"Number of letters capitalized: {cap_count}")
        print(f"Edited text: {text}")
    elif choice == 'r':
        text = replace_punctuation(text)
        print(f"Edited text: {text}")
    elif choice == 's':
        text = shorten_space(text)
        print(f"Edited text: {text}")
    return text

if __name__ == '__main__':
    # (1) Get user input
    text = input("Enter a sample text:\n")
    print(f"\nYou entered: {text}")

    # (4) Menu loop
    while True:
    print_menu()
    choice = input("Choose an option:\n").strip().lower()

    while choice not in ['c', 'w', 'f', 'r', 's', 'q']:
        choice = input("Choose an option:\n").strip().lower()

    if choice == 'q':
        break

    text = execute_menu(choice, text)

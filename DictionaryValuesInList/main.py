def count_char_get_method(text_):
    characters = dict()
    for char in text_:
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    return characters


def char_list(text_):
    dictionary = count_char_get_method(text_)
    new_dictionary = dict()

    for key in dictionary:
        value = dictionary[key]

        if value not in new_dictionary:
            new_dictionary[value] = [key]
        else:
            new_dictionary[value].append(key)

    return new_dictionary


text = input("Please insert a string: ")
char_dict = char_list(text)
print(char_dict)

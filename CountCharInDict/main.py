def count_char(text_):
    characters = dict()

    for char in text_:
        if char.isalpha():
            if char in characters.keys():
                characters[char] += 1
            else:
                characters[char] = 1

    return characters


def count_char_get_method(text_):
    characters = dict()
    for char in text_:
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    return characters


text = input("Please insert a string: ")
char_dict = count_char_get_method(text)
print(char_dict)

def swap_case(string):
    result = []
    for letter in string:
        if letter.isupper():
            result.append(letter.lower())
        elif letter.islower():
            result.append(letter.upper())
        else:
            result.append(letter)
    return "".join(result)

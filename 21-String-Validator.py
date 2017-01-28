def has_alnum(string):
    for _ in string:
        if _.isalnum():
            return True
    return False
def has_alpha(string):
    for _ in string:
        if _.isalpha():
            return True
    return False
def has_digit(string):
    for _ in string:
        if _.isdigit():
            return True
    return False
def has_lower(string):
    for _ in string:
        if _.islower():
            return True
    return False
def has_upper(string):
    for _ in string:
        if _.isupper():
            return True
    return False
if __name__ == '__main__':
    s = raw_input()
    print has_alnum(s)
    print has_alpha(s)
    print has_digit(s)
    print has_lower(s)
    print has_upper(s)

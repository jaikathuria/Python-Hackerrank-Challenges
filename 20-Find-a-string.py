def has_substring(string, sub_string):
    if string[:len(sub_string)] == sub_string:
        return True
    else:
        return False
def count_substring(string, sub_string):
    count = 0
    for _ in xrange(len(string)):
        if has_substring(string[_:], sub_string):
            count += 1
    return count

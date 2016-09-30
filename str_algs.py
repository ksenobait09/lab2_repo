def reverse_string(string):
    new_string = ''
    length = len(string)
    i = 1
    for abc in string:
        new_string += string[length - i]
        i += 1
    return new_string

print(reverse_string('hello, world'))

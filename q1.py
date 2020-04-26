import sys


def replace_spaces(sentence):
    # string to list
    list_char = [c for c in sentence]

    # remove spaces from the beginning
    while ' ' in list_char[0]:
        del list_char[0]

    # remove spaces from the end
    while ' ' in list_char[len(list_char) - 1]:
        del list_char[-1]

    # change space to &32 char and convert list to string again
    result = ''
    for i in list_char:
        if ' ' in i:
            i = '&32'
        result += i

    return result


if __name__ == "__main__":
    sentence = '   Try to understand what happened   '
    sys.exit(replace_spaces(sentence))

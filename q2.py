import sys


def is_partial_permutation(str_one, str_two):
    first_letter_one = str_one[0]
    first_letter_two = str_two[0]
    last_letter_one = str_one[-1]
    last_letter_two = str_two[-1]

    # check if the fisrt letters are equals
    if first_letter_one != first_letter_two:
        return False

    # check if the sentences are the same length
    if len(str_one) != len(str_two):
        return False

    # check if the sentences has 3 letters at least
    if len(str_one) < 3 and len(str_two) < 3:
        return False

    # case when the sentences has 3 letters
    if len(str_one) == 3 and len(str_two) == 3:
        if last_letter_one != last_letter_two:
            return True
        else:
            return False

    # case when the sentences has more than 3 letters
    if len(str_one) > 3 and len(str_two) > 3:
        if str_one[1:-1] == str_two[1:-1]:
            return False
        else:
            return True


if __name__ == "__main__":
    str_1 = 'first'
    str_2 = 'fristt'
    sys.exit(print(is_partial_permutation(str_1, str_2)))

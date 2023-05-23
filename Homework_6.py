import random
import string
import time


def sum_of_list_items(arr):
    total_sum = 0
    for item in arr:
        if isinstance(item, int):
            total_sum += item
        elif isinstance(item, list):
            total_sum += sum_of_list_items(item)
    return total_sum


def cycle_words(words, output_length):
    cycled_words = []
    item_index = 0
    while len(cycled_words) < output_length:
        if item_index < len(words):
            cycled_words += words[item_index]
            item_index += 1
        else:
            item_index = 0
    return cycled_words


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return

        time.sleep(0.1)


def password_cracker():
    cracked_pass = ''
    for char in PASSWORD:
        for cracked_char in string.ascii_letters:
            if cracked_char == char:
                cracked_pass += cracked_char
    return cracked_pass


# check:
if __name__ == '__main__':
    assert sum_of_list_items([]) == 0
    assert sum_of_list_items([1, 2]) == 3
    assert sum_of_list_items([1, [2, 3, [4], [5, 6, [7]]]]) == 28

    assert cycle_words(['a', 'b', 'c'], 7) == ['a', 'b', 'c', 'a', 'b', 'c', 'a']
    assert cycle_words(['a', 'b', 'c'], 1) == ['a']
    assert cycle_words(['a', 'b', 'c'], 0) == []

    assert password_cracker() == PASSWORD

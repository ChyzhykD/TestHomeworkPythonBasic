# import random
# import string
# import time


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


# check the function:
if __name__ == '__main__':
    assert sum_of_list_items([]) == 0
    assert sum_of_list_items([1, 2]) == 3
    assert sum_of_list_items([1, [2, 3, [4], [5, 6, [7]]]]) == 28

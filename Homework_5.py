sentence = "My name is Dmytro."
print(sentence[::-1])
sentence_length = len(sentence)
print(sentence_length)
sentence_list = list(sentence)
print(sentence_list)
every_third_letter = "|".join(sentence_list[2::3])
print(every_third_letter)


def count_symbols_without_count(string):
    symbol_count = {}
    for char in string:
        if char in symbol_count:
            symbol_count[char] += 1
        else:
            symbol_count[char] = 1
    return symbol_count


def count_symbols_with_count(string):
    symbol_count = {}
    for char in string:
        symbol_count[char] = string.count(char)
    return symbol_count


print(count_symbols_without_count(sentence))
print(count_symbols_with_count(sentence))


def show_longest_string(strings):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


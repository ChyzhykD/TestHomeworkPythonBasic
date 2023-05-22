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


# Example of usage:
print(count_symbols_without_count(sentence))
print(count_symbols_with_count(sentence))


def show_longest_string(strings):
    longest_string = ""
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


# Example of usage:
list_of_strings = ["bomb", "aircraft", "bullet"]
print(show_longest_string(list_of_strings))


def divide_and_glue(string, delimiter):
    words = string.split(delimiter)
    sorted_words = sorted(words)
    return delimiter.join(sorted_words)


# Example of usage:
string_with_delimiter = "l/o/g/q/a/c/e/b"
custom_delimiter = "/"
print(divide_and_glue(string_with_delimiter, custom_delimiter))


def print_string_by_ascii(numbers):
    ascii_string = ""
    for num in numbers:
        ascii_string += chr(num)
    print(ascii_string)


# Example of usage:
encoded_list = [119, 101, 108, 108, 32, 100, 111, 110, 101]
print_string_by_ascii(encoded_list)

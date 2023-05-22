sentence = "My name is Dmytro."
print(sentence[::-1])
sentence_length = len(sentence)
print(sentence_length)
sentence_list = list(sentence)
print(sentence_list)
every_third_letter = "|".join(sentence_list[2::3])
print(every_third_letter)

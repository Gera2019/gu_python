# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.


num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
              'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate_adv(word):
    if word[0].isupper():
        return num_dict.get(word.lower()).capitalize()
    else:
        return num_dict.get(word)



print(num_translate_adv('EiGHt'))
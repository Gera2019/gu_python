# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
from typing import List

names = ['Екатерина', 'Евгений', 'Алексей', 'Андрей', 'Денис', 'Алиса', 'Ольга']
names_adv = ['Екатерина Стрельникова', 'Евгений Сирин', 'Алексей Шаров', 'Денис Бердников', 'Дмитрий Булычев', 'Денис Ширин',
             'Алиса Быкова', 'Ольга Сорокина']
"""
Функция thesaurus(*args) для каждого значения сортированного списка аргументов образует список элементов, начинающиеся 
с одной и той же буквы и затем формирует словарь, где ключ - первая буква элемента, а значение - список элементов
"""

def thesaurus(*args):
    person_dict = {}
    for item in sorted(args):
        first_char = item[0]
        name_value = filter(lambda n: n.startswith(first_char), args)
        person_dict.setdefault(first_char, [*name_value])
    return person_dict

"""
Функция thesaurus_adv(*args) из каждого значения сортированного списка аргументов образует список 
элементов (имя, фамилия), а затем формирует словарь, где ключ - первая буква фамилии, а значение - словари, 
где ключ - первая буква имени, а значение Имя Фамилия
"""

def thesaurus_adv(*args):
    person = {}

    for item in sorted(args):
        first_char = item.split(' ')[1][0]
        person.setdefault(first_char, thesaurus(*filter(lambda x: x.split(' ')[1].startswith(first_char), args)))
        # print(person)
    return person


print(thesaurus_adv(*names_adv))



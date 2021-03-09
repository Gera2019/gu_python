tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Василий', 'Денис']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

# вывести вторым значением None, если учеников в списке больше, чем список классов
tutor_klasses = ((t, k) for t, k in zip(tutors, klasses + ['None' for el in range(len(tutors) - len(klasses))]))

print(type(tutor_klasses))
print(*tutor_klasses)

message = ''
for i in range(40):
    if i % 10 == 1 and i != 11:
        message = 'процент'
    elif i % 10 in range(2, 5) and i not in range(12, 15):
        message = 'процента'
    elif i % 10 in range(5, 10) or i == 0:
        message = 'процентов'

    print(f'{i} {message}')

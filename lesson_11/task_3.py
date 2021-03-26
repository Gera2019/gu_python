class NumCheck(Exception):
    def __init__(self, msg):
        self.msg = msg


l = []

inp_data = input('Введите число: ')
while inp_data != 'stop':
    try:
        if not inp_data.isnumeric():
            raise NumCheck('Ошибка. Вы ввели не число!')
        else:
            l.append(inp_data)

    except NumCheck as e:
        print(e)
    inp_data = input('Введите число: ')
print('Итоговый список: ', l)

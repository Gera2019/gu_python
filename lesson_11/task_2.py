class DivToZero(Exception):
    def __init__(self, msg):
        self.msg = msg


# test section
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
try:
    if y == 0:
        raise DivToZero('Ошибка! Деление на ноль!')
    else:
        result = x / y
        print(result)
except DivToZero as e:
    print(e)

else:
    print('Деление прошло успешно')

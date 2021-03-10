from sys import argv

# функцмя, которая читает по одному байту и записывает их со смещением вправо на величину offset
def shift_right(position, offset):
    end = f.seek(0, 2)
    new_end = end + offset
    while new_end >= (position + offset) and end >= position:
        f.seek(end - 1)
        b = f.read(1)
        f.seek(new_end - 1)
        f.write(b)
        new_end -= 1
        end -= 1

# функцмя, которая читает по одному байту и записывает их со смещением влево на величину offset
def shift_left(position, offset):
    end = f.seek(0, 2)
    start = position
    new_start = position + offset
    while new_start <= (end + offset) and start <= end:
        f.seek(start)
        b = f.read(1)
        f.seek(new_start)
        f.write(b)
        new_start += 1
        start += 1
    f.seek(end + offset)        # избавляемся от строк, которые остались после копирования со смещением
    f.truncate()


def edit_sale(number, value):
    line_error = True   # переменнная-флаг, которая определяет, есть ли заданный пользователем номер строки в файле
    last_line = 0   # переменная, для хранения номера последней строки, чтобы подсказать пользователю, сколько в файле строк существует

    for index, line in enumerate(f):
        if index == number - 1:
            line_error = False
            replace_point = f.tell() - len(line)
            length_diff = len(value) - len(line)
            if length_diff > 0:
                shift_right(f.tell(), length_diff)
            else:
                shift_left(f.tell(), length_diff)
            f.seek(replace_point)
            f.write(value)
            break
        last_line = index + 1

    if line_error: print('The line', number, 'doesn\'t exist\nThe last line is', last_line)


with open('bakery.csv', 'rb+') as f:
    number = int(argv[1])
    value = (argv[2] + '\n').encode(encoding='utf-8')  # преобразуем текстовое значение в байт-код
    edit_sale(number, value)


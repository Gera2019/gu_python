from collections import defaultdict

class OfficeEqpmt:
    type = ''
    def __init__(self, name, vendor):
        self.name = name
        self.vendor = vendor

    def __str__(self):
        return f'{self.type} {self.vendor.capitalize()} {self.name.capitalize()}'

    @property
    def _data(self):
        return (self.type, self.vendor, self.name)

class Printer(OfficeEqpmt):
    type = 'printer'

class Scanner(OfficeEqpmt):
    type = 'scanner'

class MFU:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    type = 'MFU'

class Storage:
    total_cnt = 0
    _shelf = defaultdict(list)
    _location = 'Storage'

    @staticmethod
    def __data_validation(data):
        if not isinstance(data[0], OfficeEqpmt) or not isinstance(data[1], int):
            return False
        else:
            return True

    @classmethod
    def storage_in(self, equipment, quantity):
        self.__item_quantity = [equipment, quantity]

        try:
            if self.__data_validation(self.__item_quantity):
                self.total_cnt += 1 * quantity
                self._shelf[equipment._data[0]].append([equipment, quantity, self._location])
            else:
                raise TypeError
        except TypeError:
            print(f'The data type is invalid for {equipment}, please check and try again')

    @classmethod
    def storage_out(self, equipment, quantity, location):
        self.__item_quantity = [equipment, quantity]
        self.total_cnt -= 1 * quantity

        try:
            if self.__data_validation(self.__item_quantity):
                list_eq = self._shelf[equipment._data[0]]
                for el in list_eq:
                    if el[0] == equipment:
                        el[1] -= quantity

                list_eq.append((equipment, quantity, location))
            else:
                raise TypeError
        except TypeError:
            print(f'The data type is invalid for {equipment}, please check and try again')

    @classmethod
    def get_info(self, args=None):
        if args:
            for el in self._shelf[args]:
                print(f'Position: {el[0]}, Quantity: {el[1]}, Location: {el[2]}')
        else:
            for item in self._shelf.values():
                for el in item:
                    print(f'Position: {el[0]}, Quantity: {el[1]}, Location: {el[2]}')


# test section
# Создание экзепляров из подклассов Принтер, Сканер и МФУ
p1 = Printer('R450', 'epson')
p2 = Printer('H7000', 'epson')
s = Scanner('U789', 'epson')
m = MFU('S2000', 'futjitsu')

# Проверка метода складка, который фиксирует прием техники
# В качестве параметров метод принимает объект из класса офисной техники и количество данной единицы товара
Storage.storage_in(p1, 1)
Storage.storage_in(p2, 2)
Storage.storage_in(s, 8)

# объект m  не является объектом офисной техники, проверка, что валидация данных отрабатывает
# во втором случае, количество не является типом int

Storage.storage_in(m, 2)
Storage.storage_in(m, '3')
print('-' * 10)

# Метод get_info() позволяет вывести информацию о всех товарах или только о конкретных видах,
# например get_info('printer') выведет информацию только о принтерах
Storage.get_info()
print('-' * 10)
Storage.get_info('scanner')
print('-' * 10)

# Проверка метода отпуска товара в отделы
Storage.storage_out(p2, 1, 'Бухгалтерия')
Storage.storage_out(s, 2, 'Юридический отдел')
Storage.get_info()




class Cell:
    def __init__(self, cell_number):
        self.num = int(cell_number)

    def check_type(self, other):
        try:
            if not isinstance(other, Cell):
                raise TypeError
            else:
                return True

        except TypeError:
            print('Error: The other is not type of Cell')

    def __add__(self, other):
        if self.check_type(other):
            print(Cell(self.num + other.num).num)

    def __sub__(self, other):
        if self.check_type(other):
            if self.num > other.num:
                print(Cell(self.num - other.num).num)
            else:
                print('Error: The result is less than zero')

    def __mul__(self, other):
        if self.check_type(other):
            print(Cell(self.num * other.num).num)

    def __floordiv__(self, other):
        if self.check_type(other):
            print(Cell(self.num // other.num).num)

    def make_order(self, cell_in_row):
        row = self.num // cell_in_row
        remainder = self.num % cell_in_row

        for i in range(row):
            print(rf'{cell_in_row*"*"}\n', end='')
        print('*'*remainder)


# class test
a = Cell(12)
b = Cell(2)
c = 5
a + b
a + c
b - a
a - b
a // b
b // a
a.make_order(5)
a.make_order(7)
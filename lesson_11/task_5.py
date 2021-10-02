class Complex_Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f'{self.real} + {self.imaginary}'

    def __add__(self, other):
        addition = [str(i + j) for i, j in zip(self.__data_repr(), other.__data_repr())]
        addition[-1] = addition[-1] + 'i'
        return Complex_Number(*addition)

    def __mul__(self, other):
        a = self.__data_repr()
        b = other.__data_repr()
        res_real = str(a[0] * b[0] + a[1] * b[1] * (-1))
        res_imaginary = str(a[1] * b[0] + a[0] * b [1]) + 'i'
        return Complex_Number(res_real, res_imaginary)

    def __data_repr(self):
        r = int(self.real)
        im = int(self.imaginary[:-1])
        return (r, im)

# test section

a = Complex_Number('-1', '3i')
b = Complex_Number('4', '-5i')
print(a)
print(b)
print(a + b)
print(a*b)
print(type(a+b))
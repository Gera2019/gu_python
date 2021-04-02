class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        line = ''
        for element in self.data:
            line += '|{}|\n'.format(str(element).lstrip('[').rstrip(']'))
        return line.replace(',', '')

    def __add__(self, other):
        try:
            if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
                msg = 'Matrices has incompatible dimensions'
                raise ValueError(msg)
        except ValueError as e:
            return e
        else:
            result = []
            for i in range(len(self.data)):
                result.append([])
                for j in range(len(self.data[i])):
                    result[i].append(self.data[i][j] + other.data[i][j])
            return Matrix(result)




# class test
m1 = [[31, 22], [37, 43], [51, 86]]
m2 = [[45, 7], [-5, 45]]
m3 = [[1, 4, 56, 6],[5, 34, 34, 34]]
m4 = [[67, -34, 56, -34],[6, 2, 1, 54]]

print(7*'-','Test1')
a = Matrix(m1)
b = Matrix(m2)
print(a + b)

print(7*'-','Test2')
a = Matrix(m3)
b = Matrix(m4)

print(a + b)
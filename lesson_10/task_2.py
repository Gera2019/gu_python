class Clothes:
    def __init__(self, size):
        self.size = size


class Coat(Clothes):

    def get_fabric_amount(self):
        print (round((self.size / 6.5 + 0.5), 2))


class Suit(Clothes):

    def get_fabric_amount(self):
        print(round((2 * self.size + 0.3), 2))


# class test
a = Suit(3)
a.get_fabric_amount()

b = Coat(5)
b.get_fabric_amount()
print(isinstance(a, Suit))
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self):
        print('Запуск отрисовки в режиме Pen')

class Pencil(Stationary):
    def draw(self):
        print('Запуск отрисовки в режиме Pencil')

class Handle(Stationary):
    def draw(self):
        print('Запуск отрисовки в режиме Handle')


a = Pen('pen')
a.draw()

b = Pencil('Kohinoor')
b.draw()

c = Handle('Wacom')
c.draw()
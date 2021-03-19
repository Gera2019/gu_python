class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car go')

    def stop(self):
        print('The car is stopped')

    def turn(self, direction):
        print('The car is turned', direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
           print('The speed is exceeded')
        else:
            print(self.speed)

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('The speed is exceeded')
        else:
            print(self.speed)

class PoliceCar(Car):
    pass

matiz = TownCar(80, 'red', 'matiz', False )
matiz.turn('left')
matiz.show_speed()
matiz.stop()
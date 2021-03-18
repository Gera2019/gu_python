import time

class TrafficLight:
    def running(self):
        _color = {'red': 7, 'yellow': 2, 'green': 5}

        for color, cnt in _color.items():
            print(f'{color} light is active')
            for seconds in range(cnt):
                print(f'Left {cnt - seconds} seconds')
                time.sleep(1)


a = TrafficLight()
a.running()

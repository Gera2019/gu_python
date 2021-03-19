import time

class TrafficLight:

    __base_mode = ('red', 'yellow', 'green')
    __modes = __base_mode + ('base',)

    def __init__(self, sec=(7, 2, 5)):
        self._sec = sec

    def __data_check(self, mod_chk, interval_chk):
        if mod_chk not in TrafficLight.__modes and mod_chk != 'stop':
            msg = f'The value \"{mod_chk}\" is invalid'
            raise ValueError(msg)
        t = True
        for s in interval_chk:
            t = t and isinstance(s, int)
            if not t:
                msg = f'The value \"{interval_chk}\" is invalid'
                raise ValueError(msg)

    def get_status(self):
        print('active mode:', self._mode)
        if self._mode == 'base':
            print(self._sec)

    def running(self, mode, *args):
        self._mode = mode
        if args:
            self._sec = args
        # print(self._seconds)
        try:
            self.__data_check(self._mode, self._sec)
        except ValueError as e:
            print(e)
        else:
            print(f'TrafficLight now works in {self._mode} mode')
            if self._mode in TrafficLight.__base_mode:
                print(f'Single mode: {self._mode} light is active')
            elif self._mode == 'base':
                try:
                    while True:
                        f = zip(TrafficLight.__base_mode, self._sec)
                        for col, s in f:
                            if s != 0:
                                print(f'{col} light is active')
                                # print(f'Left seconds: ')
                                for seconds in range(s):
                                    print(s - seconds)
                                    time.sleep(1)
                except KeyboardInterrupt:
                    print('TrafficLight was stopped')
                    self._mode = 'stop'

    def stop(self):
        self._mode = 'stop'
        print('TrafficLight was stopped')


# class test
print(7* '-', f'\t first instance of TrafficLight')
a = TrafficLight()
a.running('red')
print(7* '-', f'\t check status of TrafficLight')
a.get_status()


print(7* '-', f'\t another instance of TrafficLight')
b = TrafficLight()
b.running('base', 3, 0, 2)
print(7* '-', f'\b check status of TrafficLight')
b.get_status()


employers = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор '
                                                                                                        'аэлита']

for info in employers:
    person = info.split(" ")
    print(f'Привет, {person[-1].capitalize()}!')

info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in info:
    if item.isdigit():
        print(f'"{int(item):02d}"', end=' ')
    else:
        print(f'{item}', end=' ')

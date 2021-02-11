info = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx in range(len(info)):
    if info[idx].isdigit():
        info[idx] = ''.join(['"', f'{int(info[idx]):02d}', '"'])

    elif ('+' in info[idx] or '-' in info[idx]) and info[idx][1].isdigit():
        info[idx] = ''.join(['"', f'{info[idx][0]}{int(info[idx][1:]):02d}', '"'])

print(' '.join(info))

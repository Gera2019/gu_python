goods = [78.8, 89.9, 150, 134.50, 678.99, 39.99, 20.89, 77.69, 145.90, 6.90, 14.44, 156, 67.9]

for item in goods:

    print(f'{int(item):02d} руб {round((item % int(item)*100)):02d} коп', sep=",")

print(sorted(goods))
print(goods)

goods_sorted = sorted(goods).copy()
print(sorted(goods_sorted, 1, reversed()))
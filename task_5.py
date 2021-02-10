goods = [78.8, 89.9, 150, 134.50, 678.99, 39.99, 20.89, 77.69, 145.90, 6.90, 14.44, 156, 67.9]
new_list = []
for item in goods:
    rub = f'{int(item):02d} руб'
    kop = f'{round((item % int(item) * 100)):02d} коп'
    new_list.append(f'{rub} {kop}')

print(', '.join(new_list))

# Вывести цены, отсортированные по возрастанию, новый список не создавать
# (доказать, что объект списка после сортировки остался тот же)
print(sorted(goods))
print(goods)
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
goods_sorted = sorted(goods).copy()
print(list(reversed(goods_sorted)))

# Вывести цены пяти самых дорогих товаров.
print(sorted(goods)[-5:])

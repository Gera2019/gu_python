src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = set()
new_src = []

for num in src:
    if num not in tmp:
        new_src.append(num)
    elif num in new_src:
        new_src.remove(num)
    tmp.add(num)

print(new_src)

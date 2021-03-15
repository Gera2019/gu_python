import os
from collections import defaultdict
import shutil
import sys


def files_list(folder):
    for i in folder:
        for j in i[2]:
            yield (os.path.join(i[0], j))


folder = [item for item in os.walk('test_folder')]
res = {}
cnt_10 = 0
cnt_100 = 0
cnt_1000 = 0
a = set()
b = set()
c = set()

for file in files_list(folder):
    file_size = os.stat(file).st_size
    _ = os.path.split(file)[1]
    file_ext = _.split('.')[-1]

    if file_size <= 10:
        cnt_10 += 1
        a.add(file_ext)
    elif 10 <= file_size <= 100:
        cnt_100 += 1
        b.add(file_ext)
    elif file_size > 100:
        cnt_1000 += 1
        c.add(file_ext)

result = {10: (cnt_10, list(a)), 100: (cnt_100, list(b)), 1000: (cnt_1000, list(c))}
print(result)
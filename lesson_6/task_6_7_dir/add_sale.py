import sys

args = sys.argv[1]


def add_sale(item):
    with open('bakery.csv', 'a+', encoding='utf-8') as f:
        f.write(item + '\n')
    print('New value was added to bakery.csv')


add_sale(args)
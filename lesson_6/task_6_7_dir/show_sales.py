import sys

args = sys.argv[1:]


def show_sales(start = 0, stop = 0):
    for position, line in enumerate(f):
        if position + 1 >= start:
            if position + 1 == stop:
                print(line.rstrip('\n'))
                break
            print(line.rstrip('\n'))


with open('bakery.csv', 'r') as f:
    if args == []:
        show_sales()
    elif len(args) == 1:
        show_sales(int(args[0]))
    else:
        show_sales(int(args[0]), int(args[1]))

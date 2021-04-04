import sys
from itertools import islice


def show_sales(from_nr=None, to_nr=None):
    with open('bakery.csv', 'r', encoding='utf-8') as bakery_file:
        if not from_nr and not to_nr:
            line = bakery_file.readline()
            while line:
                print(line.replace('\n', ''))
                line = bakery_file.readline()
        if from_nr and to_nr:
            for line in islice(bakery_file, from_nr - 1, to_nr - 1):
                print(line.replace('\n', ''))
        if from_nr and not to_nr:
            for line in islice(bakery_file, from_nr - 1, None):
                print(line.replace('\n', ''))


if __name__ == '__main__':
    from_nr = None
    to_nr = None
    if len(sys.argv) == 2:
        from_nr = int(sys.argv[1])
    elif len(sys.argv) == 3:
        from_nr = int(sys.argv[1])
        to_nr = int(sys.argv[2])

    show_sales(from_nr, to_nr)

import sys


def edit_sale(nr, value):
    with open('bakery.csv', 'r+', encoding='utf-8') as bakery_file:
        lines = bakery_file.readlines()
        if nr > len(lines):
            return None

        lines[nr - 1] = value + '\n'
        bakery_file.seek(0)
        bakery_file.writelines(lines)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Sorry, not enough arguments')
    else:
        row = int(sys.argv[1])
        val = sys.argv[2]

        edit_sale(row, val)

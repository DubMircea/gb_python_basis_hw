import sys


def add_sale(amount):
    with open('bakery.csv', 'a', encoding='utf-8') as bakery_file:
        bakery_file.write(amount + '\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        value = sys.argv[1]
        add_sale(value)
    else:
        print(f'Sorry, not enough arguments')

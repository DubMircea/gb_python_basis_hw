class Num:
    result = []

    @classmethod
    def validate(cls, val: str):
        if val.isnumeric():
            cls.result.append(int(val))
        else:
            print(ValueError('must be number'))


def main_loop():
    numeric = Num()
    while True:

        num = input("Enter a number: ")
        if num == 'stop':
            print(numeric.result)
            break

        numeric.validate(num)


if __name__ == '__main__':
    main_loop()

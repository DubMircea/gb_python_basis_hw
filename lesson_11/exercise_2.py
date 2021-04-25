class OwnZeroDivisionError(ZeroDivisionError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'


def division(n, m):
    if m == 0:
        print(OwnZeroDivisionError(' zero division exception, introduce other number'))
        # or raise
        return

    return n / m


division(2, 0)

class Square:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Square(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > 0 and other.cells > 0:
            return Square(self.cells - other.cells)
        else:
            raise ValueError('o value')

    def __mul__(self, other):
        if self.cells > 0 and other.cells > 0:
            return Square(self.cells * other.cells)
        else:
            raise ValueError('o value')

    def __floordiv__(self, other):
        if self.cells > 0 and other.cells > 0:
            return Square(int(self.cells / other.cells))
        else:
            raise ValueError('o value')

    def __truediv__(self, other):
        if self.cells > 0 and other.cells > 0:
            return Square(self.cells // other.cells)
        else:
            raise ValueError('o value')

    def make_order(self, n):
        nr = self.cells // n
        rest = self.cells % n
        return '\n'.join(['*' * n] * nr + ['*' * rest])


square_1 = Square(9)
square_2 = Square(5)
print(square_1.make_order(5))
square_3 = square_1+square_2
print(square_3.cells)
square_4 = square_1-square_2
print(square_4.cells)
square_5 = square_1/square_2
print(square_5.cells)
square_6 = square_1*square_2
print(square_6.cells)
square_7 = square_1/square_2
print(square_7.cells)
square_8 = square_1//square_2
print(square_8.cells)

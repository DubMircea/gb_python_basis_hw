class Complex:
    def __init__(self, real, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex((self.real * other.real) - (self.imaginary * other.imaginary),
                       (self.imaginary * other.real) + (self.real * other.imaginary))

    def __str__(self):
        return f'({self.real},{self.imaginary})'


a = Complex(2, 10)
b = Complex(3, 5)

print(a + b)
print(a * b)

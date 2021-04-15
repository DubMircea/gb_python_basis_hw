class Road:
    # length, width - in m
    def __init__(self, length, width):
        if length < 1 or width < 1:
            raise ValueError('arguments must be greater than 0')

        self._length = length
        self._width = width

    # weight - in kg
    # thickness - in cm
    def calculate(self, weight, thickness):
        if weight < 1 or thickness < 1:
            raise ValueError('arguments must be greater than 0')

        return (self._length * self._width * weight * thickness) / 1000


road = Road(20, 5000)
res = road.calculate(25, 5)
print(res)

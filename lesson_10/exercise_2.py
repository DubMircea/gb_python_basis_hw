from abc import ABC, abstractmethod


class AbstractWear(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(AbstractWear):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def fabric_consumption(self):
        return self.height / 6.5 + 0.5


class Suit(AbstractWear):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def fabric_consumption(self):
        return 2 * self.size + 0.3


coat = Coat(171)
print(coat.fabric_consumption())
suit = Suit(170)
print(suit.fabric_consumption())

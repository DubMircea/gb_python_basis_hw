from collections import defaultdict


class Warehouse:
    stored = defaultdict(int)
    subdivisions = {}

    @staticmethod
    def check_for_dict(data_dict, key):
        if data_dict.get(key) is None:
            data_dict[key] = {}

        return data_dict

    @classmethod
    def equipment_reception(cls, equipment_type: str, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError('quantity must be integer')

        cls.stored[equipment_type] += quantity

    @classmethod
    def equipment_transfer(cls, subdivision, equipment_type: str, quantity: int):
        if not isinstance(quantity, int):
            raise ValueError('quantity must be integer')

        if quantity > cls.stored.get(equipment_type, 0):
            raise ValueError('Not enough equipment on warehouse')

        cls.check_for_dict(cls.subdivisions, subdivision)
        cls.check_for_dict(cls.subdivisions[subdivision], equipment_type)
        cls.subdivisions[subdivision][equipment_type] = quantity

        cls.stored[equipment_type] -= quantity


class Equipment:
    def __init__(self, serial_nr, interface):
        self.serial_nr = serial_nr
        self.interface = interface


class Printer(Equipment):
    def __init__(self, serial_nr, interface, is_multifunctional):
        super().__init__(serial_nr, interface)
        self.is_multifunctional = is_multifunctional


class Xerox(Equipment):
    def __init__(self, serial_nr, interface, is_colored):
        super().__init__(serial_nr, interface)
        self.is_colored = is_colored


class Scanner(Equipment):
    def __init__(self, serial_nr, interface, resolution):
        super().__init__(serial_nr, interface)
        self.resolution = resolution


eq = Warehouse()
print(eq.stored)
eq.equipment_reception('printer', 2)
print(eq.stored)
eq.equipment_reception('printer', 3)
print(eq.stored)

eq.equipment_transfer('managers', 'printer', 1)
print(eq.stored)

print(eq.subdivisions)

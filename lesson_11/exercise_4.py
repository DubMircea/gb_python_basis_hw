class Warehouse:
    pass


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

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'car goes')

    def stop(self):
        print(f'car stopped')

    def turn(self, direction):
        print(f'car turned to {direction}')

    def show_speed(self):
        print(f'Current speed {self.speed}')


class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 60:
            print(f'you violated speed, current speed {self.speed}')
        else:
            print(f'Current speed {self.speed}')


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if self.speed > 40:
            print(f'you violated speed, current speed {self.speed}')
        else:
            print(f'Current speed {self.speed}')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


car = Car(50, 'red', 'Lada', False)
car.go()
car.turn('Left')
car.show_speed()

town_car = TownCar(70, 'red', 'Lada', False)
town_car.go()
town_car.turn('Right')
town_car.show_speed()

work_car = WorkCar(50, 'red', 'Lada', False)
work_car.go()
work_car.turn('Left')
work_car.show_speed()
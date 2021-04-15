import time


class TrafficLight:
    __color = ''

    def running(self):
        for duration, color in zip([7, 2, 10], ['красный', 'жёлтый', 'зелёный']):
            self.__color = color
            while duration:
                print(f'{self.__color} осталось {duration} секунд')
                time.sleep(1)
                duration -= 1


traffic_light = TrafficLight()
traffic_light.running()

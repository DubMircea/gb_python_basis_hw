import re
from datetime import datetime


class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def convert(cls, data):
        if cls.validate(data):
            return datetime.strptime(data, '%d-%m-%Y').date()

    @staticmethod
    def validate(data):
        regex = re.compile('([0-9]{2}-[0-9]{2}-[0-9]{4})')
        if not regex.match(data):
            print('не валидный формат: «день-месяц-год»')
            return False
        else:
            day, month, year = map(int, data.split('-'))
            if not 31 >= day > 0:
                print('не валидный день')
                return False
            if not 12 >= month > 0:
                print('не валидный месяц')
                return False

            return True


Data.validate('01-02-2021')
print(Data.convert('01-02-2021'))

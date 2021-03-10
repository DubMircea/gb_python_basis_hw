duration_input = int(input('продолжительности в секундах:'))
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_MONTH = 31
MONTHS_IN_YEAR = 12

if duration_input <= SECONDS_IN_MINUTE:
    print(f'до минуты: {SECONDS_IN_MINUTE - duration_input} сек')
else:
    seconds = duration_input % SECONDS_IN_MINUTE
    minutes = duration_input // SECONDS_IN_MINUTE
    if minutes <= MINUTES_IN_HOUR:
        print(f'до часа: {MINUTES_IN_HOUR - minutes} мин {SECONDS_IN_MINUTE - seconds} сек')
    else:
        hours = minutes // MINUTES_IN_HOUR
        if hours <= HOURS_IN_DAY:
            print(f'до суток: {HOURS_IN_DAY - hours} час {MINUTES_IN_HOUR - minutes} мин '
                  f'{SECONDS_IN_MINUTE - seconds} сек')
        else:
            days = hours // HOURS_IN_DAY
            hours = hours - days * HOURS_IN_DAY
            minutes = minutes - (days * HOURS_IN_DAY * MINUTES_IN_HOUR + hours * MINUTES_IN_HOUR)

            if days <= DAYS_IN_MONTH:
                print(f'до месяца: {DAYS_IN_MONTH - days} дней {HOURS_IN_DAY - hours} час '
                      f'{MINUTES_IN_HOUR - minutes} мин {SECONDS_IN_MINUTE - seconds} сек')
            else:
                months = days // DAYS_IN_MONTH
                days = days - months * DAYS_IN_MONTH
                hours = hours - days * HOURS_IN_DAY
                minutes = minutes - (days * HOURS_IN_DAY * MINUTES_IN_HOUR + hours * MINUTES_IN_HOUR)

                if months and months <= MONTHS_IN_YEAR:
                    print(f'до года: {MONTHS_IN_YEAR - months} месяца {DAYS_IN_MONTH - days} '
                          f'дней {HOURS_IN_DAY - hours} час {MINUTES_IN_HOUR - minutes} мин '
                          f'{SECONDS_IN_MINUTE - seconds} сек')
                else:
                    print('Данные вне диапазона')

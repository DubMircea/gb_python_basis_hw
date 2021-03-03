PERCENT_STR = 'процент'
PERCENT_SUFFIX_A = 'а'
PERCENT_SUFFIX_OV = 'ов'

percent_input = int(input('Введите число:'))

if percent_input == 0 or percent_input <= 20:
    print(f'«{percent_input} {PERCENT_STR + PERCENT_SUFFIX_OV}»')
elif percent_input == 1:
    print(f'«{percent_input} {PERCENT_STR}»')
elif 2 <= percent_input <= 4:
    print(f'«{percent_input} {PERCENT_STR + PERCENT_SUFFIX_A}»')
else:
    print(f'К сожаленю ничево не найдено')

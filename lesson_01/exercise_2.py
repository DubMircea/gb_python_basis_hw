sum_of_numbers = 0
MAGIC_NUMBER_ADD = 17
MAGIC_NUMBER_DIVIDE = 7
POW_NUMBER = 3
EVEN_NUMBER = 2
DIVISOR = 10

for i in range(1000 + 1):
    if i % EVEN_NUMBER != 0:
        num = i ** POW_NUMBER
        temp_sum = 0

        while num // DIVISOR:
            rest = num % DIVISOR
            num = num // DIVISOR
            temp_sum += rest
            if num < DIVISOR:
                temp_sum += num

        if temp_sum % MAGIC_NUMBER_DIVIDE == 0:
            sum_of_numbers += i

        temp_sum = 0
        num = i ** POW_NUMBER + MAGIC_NUMBER_ADD

        while num // DIVISOR:
            rest = num % DIVISOR
            num = num // DIVISOR
            temp_sum += rest
            if num < DIVISOR:
                temp_sum += i

        if temp_sum % MAGIC_NUMBER_DIVIDE == 0:
            sum_of_numbers += i

print(f'Сумма чисел {sum_of_numbers}')

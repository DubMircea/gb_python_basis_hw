input_data = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for idx, elem in enumerate(input_data):
    last_idx = elem.rfind(' ', )
    name = elem[last_idx:].replace(' ', '').capitalize()

    input_data[idx] = elem[:last_idx] + ' ' + name
    print(f'Привет, {name}!')

print(f'список :{input_data}')

# second version
input_data = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for idx, elem in enumerate(input_data):
    elem_lst = elem.split()
    elem_lst[-1] = elem_lst[-1].capitalize()
    name = elem_lst[-1]

    input_data[idx] = ' '.join(elem_lst)
    print(f'Привет, {name}!')

print(f'список :{input_data}')

input_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# в "05" часов "17" минут температура воздуха была "+05" градусов
for idx, elem in enumerate(input_data):
    if elem.isdigit():
        input_data[idx] = f'{int(elem):02d}'
        if input_data[idx - 1] != '"' and input_data[idx + 1] != '"':
            input_data.insert(idx, '"')
            input_data.insert(idx + 2, '"')
    elif elem.startswith('+') or elem.startswith('-'):
        sign = elem[0]
        temp_elem = elem[1:]
        if temp_elem.isdigit():
            input_data[idx] = f'{sign}{int(temp_elem):02d}'
            if input_data[idx - 1] != '"' and input_data[idx + 1] != '"':
                input_data.insert(idx, '"')
                input_data.insert(idx + 2, '"')

print(input_data)

encounters = 0
for idx, char in enumerate(input_data):
    if char == '"':
        encounters += 1

    if char == '"' and encounters % 2 == 0:
        input_data[idx] = "'"

print(' '.join(input_data).replace('" ', '"').replace(" '", '"'))

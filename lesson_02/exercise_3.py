input_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# в "05" часов "17" минут температура воздуха была "+05" градусов
for idx, elem in enumerate(input_data):
    if elem.isdigit():
        elem = f'"{int(elem):02d}"'
        input_data[idx] = elem
    elif elem.startswith('+') or elem.startswith('-'):
        sign = elem[0]
        temp_elem = elem[1:]
        if temp_elem.isdigit():
            elem = f'"{sign}{int(temp_elem):02d}"'
            input_data[idx] = elem

print(" ".join(input_data))

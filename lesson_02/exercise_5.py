input_data = [57.8, 46.51, 97, 12, 11.34, 5.78, 5.9, 3.12, 90, 112, 453.09, 9876.9]

# for elem in input_data:
#     tem = elem * 100  # for 00 коп
#     print(f'«{int(tem // 100)} руб {int(tem % 100):02d} коп»')
#
# print(''.join(input_data))
print(', '.join((f'«{int((elem*100) // 100)} руб {int((elem*100) % 100):02d} коп»' for elem in input_data)))

# Вывести цены, отсортированные по возрастанию, новый список не создавать
print(id(input_data))
input_data.sort()
print(id(input_data))
print(input_data)

# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
sorted_input_data = sorted(input_data, reverse=True)
print(sorted_input_data)
print(id(sorted_input_data))
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print(sorted_input_data[:5])
list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_index = 0   # примем обозначение индекса последнего максимального числа
last_index = 0  # примем обозначение индекса последнего числа
last_number = list_numbers[-1]  # примем обозначение последнего числа
for i, current_number in enumerate(list_numbers):  # переберем все индексы
    max_nuber = list_numbers[max_index]  # примем обозначение последнего максимального числа
    if current_number >= max_nuber:  # найдем последнее максимальное число
        max_index = i
    if current_number == last_number:  # найдем последнее число
        last_index = i
list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index]  # поменяем числа
print(list_numbers)

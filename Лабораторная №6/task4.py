import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        list_dict = []  # создаем список словарей
        for index, line in enumerate(f):
            values = line.strip(new_line).split(delimiter)  # формируем значения из строк
            if index == 0:
                heads = values  # сохраняем значения как заголовоки, если первая строка
                continue
            list_dict.append({})  # добавляем словарь в список словарей

            for i, _ in enumerate(heads):
                list_dict[-1][heads[i]] = values[i]  # добавляем в словарь заголовок
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))


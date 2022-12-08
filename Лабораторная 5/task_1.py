from pprint import pprint


def list_dict(i: int) -> dict:
    return {"bin": bin(i),  # возвращаем функцию ввиде словаря
            "dec": i,
            "hex": hex(i),
            "oct": oct(i)}


pprint([list_dict(i) for i in range(16)])  # печатем список словарей

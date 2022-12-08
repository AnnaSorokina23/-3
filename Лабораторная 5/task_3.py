from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int = 8) -> str:
    random_password = sample((*ascii_uppercase, *ascii_lowercase, *digits), n)  # генирируем случайные символы
    return "".join(random_password)  # возрвращаем функцию ввиде пароля из объединенных случайных символов


print(get_random_password())

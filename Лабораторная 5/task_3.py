from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n: int = 8) -> str:
    random_password = sample((*ascii_uppercase, *ascii_lowercase, *digits), n)
    return "".join(random_password)


print(get_random_password())

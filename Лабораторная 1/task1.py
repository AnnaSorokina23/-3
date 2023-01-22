import doctest


class Cloth:
    def __init__(self, amount_of_cloth: int):
        """
        Создание и подготовка к работе объекта "Ткань"

        :param amount_of_cloth: Имеющееся количество ткани

        Примеры:
        >>> cloth = Cloth(2)  #инициализация экземпляра класса
        """
        if not isinstance(amount_of_cloth, int):
            raise TypeError("Количество ткани должно быть типа int")
        if amount_of_cloth <= 0:
            raise ValueError("Количество ткани должно быть положительным числом")
        self.amount_of_cloth = amount_of_cloth

    def amount_short_dress(self, amount_for_short_dress: int) -> int:
        """
        Функция, которая считает сколько можно сшить коротких платьев

        :param amount_for_short_dress: Количество ткани необходимое для короткого платья

        :raise ValueError: Если имеющееся количество ткани меньше, чем требуется для короткого платья, то вызываем ошибку

        Примеры:
        >>> cloth = Cloth(2)
        >>> cloth.amount_short_dress(1)
        """
        if not isinstance(amount_for_short_dress, int):
            raise TypeError("Количество ткани должно быть типа int")
        if amount_for_short_dress <= 0:
            raise ValueError("Количество ткани должно быть положительным числом")
        ...

    def amount_long_dress(self, amount_for_long_dress: int) -> int:
        """
        Функция, которая считает сколько можно сшить длинных платьев

        :param amount_for_long_dress: Количество ткани необходимое для длинного платья

        :raise ValueError: Если имеющееся количество ткани меньше, чем требуется для длинного платья, то вызываем ошибку

        Примеры:
        >>> cloth = Cloth(2)
        >>> cloth.amount_long_dress(2)
        """
        if not isinstance(amount_for_long_dress, int):
            raise TypeError("Количество ткани должно быть типа int")
        if amount_for_long_dress <= 0:
            raise ValueError("Количество ткани должно быть положительным числом")
        ...


class Site:
    def __init__(self, site_length: int, site_width: int):
        """
        Создание и подготовка к работе объекта "Участок"

        :param site_length: Длина участка
        :param site_width: Ширина участка

        Примеры:
        >>> site = Site(20, 30) #инициализация экземпляра класса
        """
        if not isinstance(site_length, int):
            raise TypeError("Длина участка должна быть типа int")
        if site_length <= 0:
            raise ValueError("Длина участка должна быть положительным числом")
        self.site_length = site_length

        if not isinstance(site_width, int):
            raise TypeError("Ширина участка должна быть типа int")
        if site_width <= 0:
            raise ValueError("Ширина участка должна быть положительным числом")
        self.site_width = site_width

    def perimeter(self) -> int:
        """
        Функция, которая считает периметр участка

        :return: Периметр участка

        Примеры:
        >>> site = Site(20, 30)
        >>> site.perimeter()

        100
        """
        ...

    def area(self) -> int:
        """
        Функция, которая считает площадь участка

        :return: Площадь участка

        Примеры:
        >>> site = Site(20, 30)
        >>> site.area()

        600
        """
        ...


class Garden:
    def __init__(self, trees: int):
        """
        Создание и подготовка к работе объекта "Сад"

        :param trees: Количество деревьев в саду

        Примеры:
        >>> garden = Garden(10) # инициализация экземпляра класса
        """
        if not isinstance(trees, int):
            raise TypeError("Количество деревьев должно быть типа int")
        if trees <= 0:
            raise ValueError("Количество деревьев должно быть положительным числом")
        self.trees = trees

    def cut_down_trees_to_garden(self, old_trees: int) -> None:
        """
        Вырубка деревьев в саду

        :param old_trees: Количество старых деревьев

        :return: Количество деревьев в саду

        Примеры:
        >>> garden = Garden(10)
        >>> garden.cut_down_trees_to_garden(1)

        9
        """
        if not isinstance(old_trees, int):
            raise TypeError("Количество старых деревьев должно быть типа int")
        if old_trees <= 0:
            raise ValueError("Количество старых деревьев должно быть положительным числом")
        ...

    def plant_trees_to_garden(self, new_trees: int) -> None:
        """
        Посадка деревьев в саду

        :param new_trees: Количество новых деревьев

        :return: Количество деревьев в саду

        Примеры:
        >>> garden = Garden(10)
        >>> garden.plant_trees_to_garden(3)

        13
        """
        if not isinstance(new_trees, int):
            raise TypeError("Количество новых деревьев должно быть типа int")
        if new_trees <= 0:
            raise ValueError("Количество новых деревьев должно быть положительным числом")
        ...


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации

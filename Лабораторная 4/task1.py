class Biathlon:
    """ Базовый класс "Биатлон" """

    def __init__(self, name_biathlete: str, country: str, number_of_misses: int):
        """
        Создание и подготовка к работе объекта "Биатлон"
        :param name_biathlete: Имя биатлониста
        :param country: Страна
        :param number_of_misses: Количество промахов
        Пример:
        >>> biathlon = Biathlon("Эдуард Латыпов", "Россия", 2)
        """
        self._name_biathlete = name_biathlete
        self._country = country
        self._number_of_misses = number_of_misses

    @property
    def name_biathlete(self) -> str:
        return self._name_biathlete

    @property
    def country(self) -> str:
        return self._country

    @property
    def number_of_misses(self) -> int:
        return self._number_of_misses

    @number_of_misses.setter
    def number_of_misses(self, misses: int) -> None:
        if not isinstance(misses, int):
            raise TypeError("Количество промахов должно быть типа int")
        if misses <= 0:
            raise ValueError("Количество промахов должно быть положительным числом")
        self._number_of_misses = misses

    def __str__(self):
        return f"Последние новости Биатлона! Биатлонист{self._name_biathlete} из {self._country} в гонке сегодня совершил {self._number_of_misses} промаха!"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name_biathlete!r}, country={self._country!r},  number_of_misses={self._number_of_misses!r})"

    def is_clean_shooting(self) -> str:
        """
        Функция которая проверяет была ли стрельба биатлониста чистой
        :return: Есть ли промахи

        Пример:
        >>> biathlon = Biathlon ("Эдуард Латыпов", "России", 2)
        >>> biathlon.is_clean_shooting()
        'Есть промахи!'
        """
        if self._number_of_misses == 0:
            return 'Чистая стрельба!'
        if self._number_of_misses > 0:
            return 'Есть промахи!'

    def number_of_penalty_loop(self) -> int:
        """
        Функция которая оперделяет количество штрафных кругов, которые пробежал биатлонист
        :return: штрафные круги
        Пример:
        >>> biathlon = Biathlon("Эдуард Латыпов", "России", 2)
        >>> biathlon.number_of_penalty_loop()
        2
        """
        return self._number_of_misses  # Количество штрафных кругов равно количеству промахов


class Relay(Biathlon):
    """Дочерний класс "Эстафета" """
    def __init__(self, name_biathlete: str, country: str, number_of_misses: int, number_of_stage: int):
        """
        Создание и подготовка к работе дочернего класса "Эстафета".
        Парметры наследуются из базового класса
        Также добавлен новый параметр
        :param number_of_stage: Номер этапа

        Пример:
        >>> relay = Relay("Эдуард Латыпов", "Россия", 2, 4)
        """
        super().__init__(name_biathlete, country, number_of_misses)
        self._number_of_stage = number_of_stage

    @property
    def number_of_stage(self) -> int:
        return self._number_of_stage

    @number_of_stage.setter
    def number_of_stage(self, stage: int) -> None:
        if not isinstance(stage, int):
            raise TypeError("Номер этапа должн быть типа int")
        if stage <= 0:
            raise ValueError("Номер этапа должн быть положительным числом")
        self._number_of_stage = stage

    def __str__(self):
        return f"Последние новости Биатлона! Биатлонист{self._name_biathlete} из {self._country} в эстафете на {self._number_of_stage} этапе совершил{self._number_of_misses} промаха!"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name_biathlete!r}, country={self._country!r},  number_of_misses={self._number_of_misses!r}, _number_of_stage={self._number_of_stage!r} )"

    def number_of_penalty_loop(self) -> int:
        """
        Функция которая оперделяет количество штрафных кругов, которые пробежал биатлонист
        :return: штрафные круги
        Пример:
        >>> biathlon = Biathlon("Эдуард Латыпов", "России", 2, 4)
        >>> biathlon.number_of_penalty_loop()
        0
        """
        if self._number_of_misses <= 6:  # Можно потратить 6 дополнительных патронов
            return 0
        if self._number_of_misses > 6:   # Если дополнительные патроны потрачены, а мишени не закрыты, нужно бежать дополнительные круги
            return self._number_of_misses - 6


if __name__ == "__main__":
    pass


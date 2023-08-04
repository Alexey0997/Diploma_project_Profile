"""Модуль, реализующий класс Parliament (парламент), наследуемый от класса Leadership."""
from model.leadership import Leadership


class Parliament(Leadership):
    """Конструктор класса LeadershipOpponents, в котором:
        - id_stakeholders - вид стейкхолдера (политик или ученый);
        - name            - Фамилия и Имя;
        - birth_date      - дата рождения;
        - position        - должность;
        - viewpoint       - точка зрения"""
    def __init__(self, id_stakeholders, name, birth_date, position, viewpoint):
        super().__init__(kind_influence="парламент")
        self.__id_stakeholders = id_stakeholders
        self.__name = name
        self.__birth_date = birth_date
        self.__position = position
        self.__viewpoint = viewpoint

    def get_id_stakeholders(self):
        """Метод, возвращающий вид стейкхолдера."""
        return self.__id_stakeholders

    def get_name(self):
        """Метод, возвращающий Фамилию и Имя."""
        return self.__name

    def get_birth_date(self):
        """Метод, возвращающий дату рождения."""
        return self.__birth_date

    def get_position(self):
        """Метод, возвращающий должность."""
        return self.__position

    def get_viewpoint(self):
        """Метод, возвращающий точку зрения."""
        return self.__viewpoint

    def add_viewpoint(self, new_viewpoint):
        """Метод, уточняющий позицию по вопросу строительства АЭС."""
        if self.__viewpoint == '' or self.__viewpoint == 'данные уточняются':
            self.__viewpoint = new_viewpoint
        else:
            self.__viewpoint = self.__viewpoint + ' + ' + new_viewpoint

    def __str__(self):
        """Метод, определяющий порядок вывода данных о стейкхолдере."""
        return f'\tСтейкхолдер:    {self.get_kind_influence()}\n' \
               f'\tДолжность:      {self.__position}\n' \
               f'\tИмя:            {self.__name}\n' \
               f'\tДата рождения:  {self.__birth_date}\n' \
               f'\tПозиция по АЭС: {self.__viewpoint}'

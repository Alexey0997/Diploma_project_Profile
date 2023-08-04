"""Модуль, реализующий класс Leadership (политики), наследуемый от класса Stakeholders."""
from model.stakeholders import Stakeholders


class Leadership(Stakeholders):
    """Конструктор класса Leadership, в котором:
        - id_type           - индивидуальный идентификатор стейкхолдера;
        - type_stakeholders - описание идентификатора (типа) стейкхолдера;
        - kind_influence     - влияние на проект (сторонник, противник, нейтральная позиция)."""
    def __init__(self, kind_influence):
        super().__init__(id_type=1, type_stakeholders="политик")
        self.__kind_influence = kind_influence

    def get_id_type(self):
        """Метод, возвращающий индивидуальный идентификатор стейкхолдера (1)."""
        return 1

    def get_type_stakeholders(self):
        """Метод, возвращающий описание типа стейкхолдера."""
        return "политик"

    def get_kind_influence(self):
        """Метод, возвращающий тип влияния на проект."""
        return self.__kind_influence


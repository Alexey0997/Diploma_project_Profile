"""Модуль, реализующий класс Scientists (ученые), наследуемый от класса Stakeholders."""
from model.stakeholders import Stakeholders


class Scientists(Stakeholders):
    """Конструктор класса Scientists, в котором:
        - id_type           - индивидуальный идентификатор ученого;
        - type_stakeholders - описание идентификатора (типа) ученого;
        - kind_stakeholders - влияние на проект."""
    def __init__(self, kind_influence):
        super().__init__(id_type=2, type_stakeholders="ученый")
        self.kind_influence = kind_influence

    def get_id_type(self):
        """Метод, возвращающий индивидуальный идентификатор стейкхолдера (2)."""
        return 2

    def get_type_stakeholders(self):
        """Метод, возвращающий описание идентификатора (типа) стейкхолдера."""
        return "ученый"

    def get_kind_influence(self):
        """Метод, возвращающий тип влияния на проект."""
        return self.kind_influence


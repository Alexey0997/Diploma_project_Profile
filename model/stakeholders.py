"""Модуль, реализующий родительский класс Stakeholders."""
from abc import ABC, abstractmethod


class Stakeholders(ABC):
    """Конструктор класса Stakeholders, в котором:
        - id_type      - индивидуальный идентификатор типа стейкхолдера;
        - type_stakeholders - описание типа стейкхолдера."""
    def __init__(self, id_type, type_stakeholders):
        self.__id_type = id_type
        self.__type_stakeholders = type_stakeholders

    @abstractmethod
    def get_id_type(self):
        """Абстрактный метод, возвращающий индивидуальный идентификатор типа стейкхолдера (1 или 2)."""

    @abstractmethod
    def get_type_stakeholders(self):
        """Абстрактный метод, возвращающий описание типа стейкхолдера (политик или ученый)."""

"""Модуль реализует абстрактный класс View"""
from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def set_presenter(self, presenter):
        """Aбстрактный метод принимает экземпляр класса Presenter в качестве аргумента."""

    @abstractmethod
    def start(self):
        """Aбстрактный метод настраивает и запускает консольное приложение."""
        
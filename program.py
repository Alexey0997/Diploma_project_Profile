"""Модуль реализует класс Program, обеспечивающий запуск всех элементов программы."""
from db_manager.sqlite_manager import SqLiteManager
from model.stakeholders_registry import StakeholdersRegistry
from presenter.presenter import Presenter
from view.console import Console


class Program:
    def start(self):
        self.view.start()

    def __init__(self):
        self.registry = StakeholdersRegistry()
        self.view = Console()
        self.data = SqLiteManager('stakeholders.db')
        Presenter(self.view, self.registry, self.data)


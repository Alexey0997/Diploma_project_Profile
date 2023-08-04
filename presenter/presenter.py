"""Модуль, реализующий класс Presenter."""
from db_manager.sqlite_manager import SqLiteManager
from model import StakeholdersRegistry
from view.abstract_view import View


class Presenter:
    """Конструктор класса Presenter."""
    def __init__(self, view: View, log_registry: StakeholdersRegistry, data: SqLiteManager):
        self.view = view
        self.log_registry = log_registry
        self.view.set_presenter(self)
        self.data = data

    def read_db(self):
        """Метод подключения к базе данных."""
        return self.data.read_db(self.log_registry)

    def get_table_registry(self):
        """Метод вывода журнала регистрации стейкхолдеров."""
        return self.log_registry.tabl_registry

    def size_registry(self):
        """Метод определения количества элементов в регистре."""
        return self.log_registry.number_of_stakeholders()

    def all_kind_leadership(self):
        """Метод вывода данных о доступных подклассах leadership."""
        return self.log_registry.list_kind_leadership()

    def all_kind_scientists(self):
        """Метод вывода данных о доступных подклассах scientists."""
        return self.log_registry.list_kind_scientists()

    def add_stakeholder(self, kind, name, birth_date, position, viewpoint):
        """Метод вывода данных о стейкхолдере."""
        self.log_registry.add_stakeholder(kind, position, name, birth_date, viewpoint)

    def save_stakeholder(self, type_id, kind, name, birth_date, position, viewpoint):
        """Метод сохранения изменений в базе данных."""
        return self.data.save_stakeholder(type_id, kind, position, name, birth_date, viewpoint)

    def find_stakeholder(self, index):
        """Метод вывода данных о стейкхолдере по индексу."""
        return self.log_registry.find_stakeholder(index)

    def get_viewpoint(self, index):
        """Метод вывода данных о позиции стейкхолдера по строительству АЭС."""
        return self.log_registry.get_viewpoint(index)

    def add_viewpoint(self, index, viewpoint):
        """Метод добавлении данных о корректировке или детализации позиции стейкхолдера."""
        self.log_registry.add_viewpoint(index, viewpoint)

    def save_viewpoint(self, index):
        """Метод сохранения изменений в позиции стейкхолдера."""
        return self.data.save_viewpoint(index, self.log_registry)

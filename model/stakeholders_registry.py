"""Модуль реализует класс StakeholdersRegistry, предназначенный для учета стейкхолдеров."""
from tabulate import tabulate
from model.universities import Universities
from model.research_i import ResearchInstitutes
from model.think_tank import ThinkTank
from model.presidential_ad import PresidentialAdministration
from model.government import Government
from model.parliament import Parliament


class StakeholdersRegistry:
    """Конструктор класса StakeholdersRegistry, который создает новый экземпляр класса и инициализирует
       переменную __log_registry пустым списком."""
    def __init__(self):
        self.__log_registry = []

    def get_log_registry(self):
        """Метод, возвращающий журнал учета."""
        return self.__log_registry

    def number_of_stakeholders(self):
        """Метод, возвращающий количество элементов в журнале учета."""
        return len(self.__log_registry)

    def __add_presidential_ad(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления стейкхолдера в таблицу "Администрация президента"."""
        presidential_ad = PresidentialAdministration(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(presidential_ad)

    def __add_government(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления стейкхолдера в таблицу "Правительство"."""
        government = Government(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(government)

    def __add_parliament(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления стейкхолдера в таблицу "Парламент"."""
        parliament = Parliament(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(parliament)

    def __add_research_i(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления животного в таблицу "НИИ"."""
        research_i = ResearchInstitutes(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(research_i)

    def __add_university(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления животного в таблицу "ВУЗы"."""
        university = Universities(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(university)

    def __add_think_tank(self, position, name, birth_date, viewpoint, id_stakeholders=None):
        """Метод добавления животного в таблицу "исслед. центры"."""
        think_tank = ThinkTank(id_stakeholders, position, name, birth_date, viewpoint)
        self.__log_registry.append(think_tank)

    __function_add_stakeholder = {'администрация пр.': __add_presidential_ad,
                                  'правительство': __add_government,
                                  'парламент': __add_parliament,
                                  'наука': __add_research_i,
                                  'образование': __add_university,
                                  'исслед. центр': __add_think_tank}

    def add_stakeholder(self, kind, name, birth_date, position, viewpoint):
        """Метод добавления стейкхолдера в базу данных."""
        for key, value in self.__function_add_stakeholder.items():
            if key == kind:
                value(self, position, name, birth_date, viewpoint)
                break

    @property
    def tabl_registry(self):
        """Метод выводит данные журнала учета в табличной форме."""
        headers = ['№',
                   'СТЕЙКХОЛДЕР',
                   'КАТЕГОРИЯ',
                   'ДОЛЖНОСТЬ',
                   'ИМЯ И ФАМИЛИЯ',
                   'ДАТА РОЖДЕНИЯ',
                   'ТОЧКА ЗРЕНИЯ ПО ВОПРОСУ СТРОИТЕЛЬСТВА АЭС']
        tabl = [[i,
                 stakeholders.get_type_stakeholders(),
                 stakeholders.get_kind_influence(),
                 stakeholders.get_position(),
                 stakeholders.get_name(),
                 stakeholders.get_birth_date(),
                 stakeholders.get_viewpoint()]
                for i, stakeholders in enumerate(self.__log_registry, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="mixed_grid", stralign='left')

    def list_kind_leadership(self):
        """Метод формирования множества политиков."""
        kind_leadership = set()
        for item in self.__log_registry:
            if item.get_id_type() == 1:
                kind_leadership.add(item.get_kind_influence())
        return kind_leadership

    def list_kind_scientists(self):
        """Метод формирования множества ученых."""
        kind_scientists = set()
        for item in self.__log_registry:
            if item.get_id_type() == 2:
                kind_scientists.add(item.get_kind_influence())
        return kind_scientists

    def find_stakeholder(self, index):
        """Метод поиска стейкхолдера по индексу."""
        return self.__log_registry[index]

    def get_viewpoint(self, index):
        """Метод просмотра точки зрения."""
        return self.__log_registry[index].get_viewpoint()

    def add_viewpoint(self, index, viewpoint):
        """Метод уточнения позиции по вопросу строительства АЭС."""
        self.__log_registry[index].add_viewpoint(viewpoint)

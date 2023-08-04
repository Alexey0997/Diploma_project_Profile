"""Модуль реализует класс SqLiteManager (работа с базой данных SqLite)."""
import sqlite3
from model.universities import Universities
from model.research_i import ResearchInstitutes
from model.think_tank import ThinkTank
from model.presidential_ad import PresidentialAdministration
from model.government import Government
from model.parliament import Parliament
from model.stakeholders_registry import StakeholdersRegistry


class SqLiteManager:
    def __init__(self, path: str):
        """Конструктор класса SqLiteManager."""
        self.__path = path

    def __read_presidential_ad(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей presidential_ad."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM presidential_ad")
            rows = cursor.fetchall()
            for row in rows:
                presidential_ad = PresidentialAdministration(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(presidential_ad)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_government(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей government."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM government")
            rows = cursor.fetchall()
            for row in rows:
                government = Government(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(government)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_parliament(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей parliament."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM parliament")
            rows = cursor.fetchall()
            for row in rows:
                parliament = Parliament(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(parliament)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_research_i(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей s_supporters."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM research_i")
            rows = cursor.fetchall()
            for row in rows:
                research_i = Universities(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(research_i)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_universities(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей universities."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM universities")
            rows = cursor.fetchall()
            for row in rows:
                universities = ResearchInstitutes(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(universities)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def __read_think_tank(self, log_registry: StakeholdersRegistry):
        """Метод реализует работу с таблицей think_tank."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute("SELECT id_stakeholders, name, birth_date, position, viewpoint FROM think_tank")
            rows = cursor.fetchall()
            for row in rows:
                s_opponent = ThinkTank(row[0], row[1], row[2], row[3], row[4])
                log_registry.get_log_registry().append(s_opponent)
            return "Ok"
        except sqlite3.Error as e:
            return f"Ошибка при работе с базой данных: {e}"
        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    __function_read_animal = [__read_presidential_ad,
                              __read_government,
                              __read_parliament,
                              __read_research_i,
                              __read_universities,
                              __read_think_tank]

    def read_db(self, log_registry: StakeholdersRegistry):
        """Метод подключения к базе данных."""
        result = "Ok"
        for item in self.__function_read_animal:
            result = item(self, log_registry)
            if result.startswith('Ошибка'):
                return result
        return result
    """Указана идентичность значений на русском и английском языках."""
    __dict_kinds = {'администрация пр.': 'presidential_ad',
                    'правительство': 'government',
                    'парламент': 'parliament',
                    'наука': 'research_i',
                    'образование': 'universities',
                    'исслед. центр': 'think_tank'}

    def save_stakeholder(self, type_id, kind, position, name, birth_date, viewpoint):
        """Метод сохранения изменений в базе данных."""
        cursor = None
        connect = None
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            data = (type_id, position, name, birth_date, viewpoint)
            cursor.execute(f"INSERT INTO {self.__dict_kinds[kind]} (type_id, position, name, birth_date, viewpoint)"
                           "VALUES (?, ?, ?, ?, ?)", data)
            connect.commit()
            return "\tЗапись добавлена в базу данных."
        except sqlite3.Error as e:
            return f"\tОшибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

    def save_viewpoint(self, index, log_registry: StakeholdersRegistry):
        """Метод сохранения изменений в уточненной позиции стейкхолдера."""
        cursor = None
        connect = None
        kind = self.__dict_kinds[log_registry.get_log_registry()[index].get_kind_influence()]
        id_stakeholders = log_registry.get_log_registry()[index].get_id_stakeholders()
        try:
            connect = sqlite3.connect(self.__path)
            cursor = connect.cursor()
            cursor.execute(f"UPDATE {kind} SET viewpoint = ? WHERE __id_stakeholders = ?",
                           (log_registry.get_viewpoint(index), id_stakeholders))
            connect.commit()
            return "\tСписок команд успешно изменен."
        except sqlite3.Error as e:
            return f"\tОшибка при работе с базой данных: {e}"

        finally:
            if cursor:
                cursor.close()
            if connect:
                connect.close()

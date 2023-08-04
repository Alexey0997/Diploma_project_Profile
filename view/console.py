"""Модуль реализует класс Console, обеспечивающий взаимодействие с пользователем."""
from datetime import datetime
from view.abstract_view import View
from view.counter import Counter


class Console(View):
    __working = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        """Метод формирует главное меню и запускает алгоритмы работы с базой данных."""
        self.__working = True
        read_db = self.presenter.read_db()
        if read_db == "Ok":
            while self.__working:
                print('\n\tГЛАВНОЕ МЕНЮ:')
                print('\tОткрыть реестр стейкхолдеров         -> нажмите 1\n'
                      '\tДобавить стейкхолдера в базу данных  -> нажмите 2\n'
                      '\tВывести данные о стейкхолдере        -> нажмите 3\n'
                      '\tУточнить позицию стейкхолдера        -> нажмите 4\n'
                      '\tЗавершить работу с базой данных      -> нажмите 5\n')
                user_choice = self.__get_menu_number(5, '\tВаше решение: ')
                match user_choice:
                    case "1":
                        print("\n                                Ж У Р Н А Л    У Ч Е Т А   С Т Е Й К Х О Л Д Е Р О В")
                        print(self.presenter.get_table_registry())
                    case "2":
                        self.__add_type_stakeholder()
                    case "3":
                        self.__show_stakeholder()
                    case "4":
                        self.__add_viewpoint()
                    case "5":
                        self.__working = False
        else:
            print(read_db)

    def __add_type_stakeholder(self):
        """Метод предлагает пользователю выбрать тип животного для добавления в бузу данных"""
        print('\n\tУКАЖИТЕ ТИП СТЕЙКХОЛДЕРА, КОТОРОГО ХОТИТЕ ДОБАВИТЬ В БАЗУ ДАННЫХ:')
        print('\tПолитик                 -> нажмите 1\n'
              '\tУченый                  -> нажмите 2\n'
              '\tВозврат в главное меню  -> нажмите 3')
        user_choice = self.__get_menu_number(3, "\n\tВаше решение: ")
        match user_choice:
            case "1":
                self.__add_stakeholder(user_choice, self.presenter.all_kind_leadership())
            case "2":
                self.__add_stakeholder(user_choice, self.presenter.all_kind_scientists())
            case "3":
                return

    def __add_stakeholder(self, type_id, kinds):
        """Метод позволяет добавить экземпляр выбранного вида животных"""
        print(f'\n\tДОСТУПНЫ ДЛЯ ДОБАВЛЕНИЯ СЛЕДУЮЩИЕ ВИДЫ СТЕЙКХОЛДЕРОВ: {kinds}\n')
        kind = input('\tУкажите вид стейкхолдера, которого хотите добавить в базу данных: ').lower()
        if kind in kinds:
            position = input('\tУкажите должность: ')
            name = input('\tВведите имя и фамилию: ')
            birth_date = self.__get_date('\tВведите дату рождения стейкхолдера (ГГГГ-ММ-ДД): ')
            viewpoint = input('\tКратко запишите точку зрения по вопросу сторительства АЭС: ')
            if self.__save_stakeholder(kind, position, name, birth_date, viewpoint):
                self.presenter.add_stakeholder(kind, position, name, birth_date, viewpoint)
                print(self.presenter.save_stakeholder(type_id, kind, position, name, birth_date, viewpoint))
        else:
            print("\n\tДобавление указанного вида стейкхолдера не предусмотрено.")
            return

    @staticmethod
    def __get_menu_number(size: int, text: str):
        """Метод возвращает номер пункта меню и проверяет корректность ввода данных"""
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                return user_input
            print(f"\n\tВведено некорректное значение. Укажите число от 1 до {size}.")

    @staticmethod
    def __save_stakeholder(kind, position, name, birth_date, viewpoint):
        """Метод выводит пользователю введенные данные для проверки и принятия решения об их сохранении."""
        print(f'\n\tВы ввели следующие данные:\n'
              f'\t\tКатегория:      {kind}\n'
              f'\t\tДолжность:      {position}\n'
              f'\t\tИмя и Фамилия   {name}\n'
              f'\t\tДата рождения:  {birth_date}\n'
              f'\t\tПозиция по АЭС: {viewpoint}\n')
        user_choice = input('\tСохранить изменения? (д/н): ').lower()
        if user_choice in ['да', 'д', 'y', 'yes']:
            with Counter() as counter:
                if position != '' and name != '' and birth_date != '' and viewpoint != '':
                    counter.add()
                    print(f"\tКоличество добавленных стейкхолдеров: {counter.count}")
                else:
                    raise Exception('\tВведены некорректные значения.')
            return True
        else:
            print('\tДанные не сохранены.\n')
            return False

    @staticmethod
    def __get_date(text):
        """Метод проверяет введенную пользователем дату на соответствие формату "ГГГГ-ММ-ДД"."""
        while True:
            user_input = input(text)
            if user_input:
                try:
                    datetime.strptime(user_input, "%Y-%m-%d")
                    return user_input
                except ValueError:
                    print('\tНекорректный ввод. Укажите дату в формате "ГГГГ-ММ-ДД".')

    def __show_stakeholder(self):
        """Метод выводит сведения о стейкхолдере по номеру в регистре."""
        print("\n\tВЫВОД ДАННЫХ О СТЕЙКХОЛДЕРЕ:")
        user_input = self.__get_menu_number(self.presenter.size_registry(),
                                            "\tВведите регистранционный номер стейкхолдера: ")
        index = int(user_input) - 1
        print(f"\tВ базе данных имеются следующие сведения о стейкхолдере с номером {index + 1}:\n\t")
        print(self.presenter.find_stakeholder(index))
        return

    def __add_viewpoint(self):
        """Метод реализует уточнение точки зрения стейкхолдера по вопросу строительства АЭС."""
        print("\n\tУТОЧНЕНИЕ ТОЧКИ ЗРЕНИЯ ПО ВОПРОСУ СТОРОИТЕЛЬСТВА АЭС:")
        user_input = self.__get_menu_number(self.presenter.size_registry(),
                                            "\tВведите регистранционный номер стейкхолдера: ")
        index = int(user_input) - 1
        print(f'\tПозиция по строительству АЭС: {self.presenter.get_viewpoint(index)}.')
        user_answer = input('\tХотите уточнить позицию?(д/н): ')
        if user_answer in ['да', 'д', 'y', 'yes']:
            commands = input('\tУкажите новые данные: ')
            self.presenter.add_viewpoint(index, commands)
            print(self.presenter.save_viewpoint(index))
        else:
            print('\tОперация отклонена.')
            return

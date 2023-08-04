"""Модуль реализует класс Counter, выволняющий подсчет количества животных, добавленных в базу данных."""


class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1

    def get_count(self):
        return self.count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        print('\tСчетчик закрыт.')
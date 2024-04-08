import json
from abc import ABC, abstractmethod


class AbstractAddVacancy(ABC):
    @abstractmethod
    def save_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_data_on_criteria(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class VacancyList(AbstractAddVacancy):
    """
    Класс для сохранения и получения вакансий в файл.
    """
    def __init__(self, filename):
        self.filename = filename

    def save_vacancy(self, vacancy):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)
            file.write(f'{vacancy}\n')

    def get_data_on_criteria(self, vacancy):
        """
        Получение данных из файла по указанным критериям.
        :param vacancy:
        :return:
        """
        pass

    def delete_vacancy(self, vacancy):
        """
        Удаление вакансии из файла.
        :param vacancy:
        :return:
        """
        pass

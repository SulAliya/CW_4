from abc import ABC, abstractmethod

import requests


class AbstractAPI(ABC):
    """
    абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunterAPI(AbstractAPI):
    """
    подключаемся к API и получаем вакансии.
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def load_vacancies(self, keyword):
        params = {'text': keyword, 'page': 0, 'per_page': 100}
        json_data = requests.get(self.url, params=params).json()
        return json_data

class GetVacancy:
    def __init__(self, name, link, salary_from, salary_to, currency, responsibility):
        self.name = name
        self.link = link
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.responsibility = responsibility

    def __repr__(self):
        return (f'({self.name}\n, {self.link}\n, {self.salary_from}\n, {self.salary_to}\n, {self.currency}\n,'
                f' {self.responsibility}\n)')

    def __str__(self):
        return (f'Вакансия - {self.name}\n Ссылка - {self.link}\n Зарплата: {self.salary_from} - {self.salary_to} '
                f'{self.currency}\n '
                f'Обязанности: {self.responsibility}\n')

    def __call__(self, *args, **kwargs):
        return self.name, self.link, self.salary_from, self.salary_to, self.currency, self.responsibility

    def salary_comparison(self):
        """
        валидация данных, указана или нет зарплата.
        :return:
        """
        if not self.salary_from and not self.salary_to:
            self.salary_from = 0

    def __gt__(self, other):
        """
        сравнение вакансий между собой по зарплате.
        :param other:
        :return:
        """
        return self.salary_from > other.salary_from

    @staticmethod
    def convert_to_dict(obj):
        """
        Сериализирует объект класса VacanciesHH в формат JSON.
        :param obj: объект класса VacanciesHH
        :return: словарь с атрибутами объекта
        """
        if isinstance(obj, GetVacancy):
            return obj.__dict__
        return obj

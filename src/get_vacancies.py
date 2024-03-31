class GetVacancy:
    def __init__(self, name, link, salary, description):
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description

    def __str__(self):
        return f'Вакансия {self.name}\n Ссылка {self.link}\n Зарплата: {self.salary}\n  Описание: {self.description}'

    def salary_comparison(self):
        """
        валидация данных, указана или нет зарплата.
        :return:
        """
        if not isinstance(self.salary, float):
            self.salary = 'Зарплата не указана'

    def __ge__(self, other):
        """
        сравнение вакансий между собой по зарплате.
        :param other:
        :return:
        """
        return self.salary >= other.salary

import pytest
from src.get_vacancies import GetVacancy


@pytest.fixture
def test_getvacancy():
    vacancies = [
        GetVacancy(name="Test Name", link="Test link", salary_from="Test Salary_from", salary_to="Test Salary_to",
                   currency="Test Currency", responsibility="Test responsibility"),  # 0
        GetVacancy(name="Администратор в учебный центр", link="https://hh.ru/vacancy/95422523", salary_from=1500000,
                   salary_to=5000000, currency="UZS",
                   responsibility="Регистрация так же новых студентов и организация учебного процесса. "
                                  "Координация работы <highlighttext>преподавателей</highlighttext>, "
                                  "расписание занятий, поддержка в организационных вопросах. "),  # 1
        GetVacancy(name="Frontend-разработчик (Middle)", link="https://hh.ru/vacancy/96416474", salary_from=90000,
                   salary_to="null", currency="RUR",
                   responsibility="Поддерживать имеющийся функционал. "
                                  "Разрабатывать новый функционал и совершенствовать старый на базе UX/UI макетов. "
                                  "Интегрировать frontend и серверный API."),  # 2
        GetVacancy(name="Онлайн учитель английского языка", link="https://hh.ru/vacancy/94762027", salary_from=200000,
                   salary_to=300000, currency="KZT",
                   responsibility="Проведение групповых и индивидуальных занятий взрослым и детям на уровнях от "
                                  "Beginner до Advanced. — Проведение занятий согласно программе и расписании. — "), # 3
        GetVacancy(name="Стажер-разработчик Python", link="https://hh.ru/vacancy/95989169", salary_from=200,
                   salary_to="null", currency="BYR",
                   responsibility="Отработка/практика для студентов с последующим распределением в организацию. "
                                  "Обязанности: Работать предстоит с созданием приложений,"
                                  " дополнений к CRM системам, панелей...")  # 4
    ]
    return vacancies
def test_init_getvacancy(test_getvacancy):
    vacancy_2 = test_getvacancy[1]
    assert vacancy_2.name == 'Администратор в учебный центр'
    assert vacancy_2.link == 'https://hh.ru/vacancy/95422523'
    assert vacancy_2.salary_from == 1500000
    assert vacancy_2.salary_to == 5000000
    assert vacancy_2.currency == 'UZS'
    assert vacancy_2.responsibility == ('Регистрация так же новых студентов и организация учебного процесса. '
                                        'Координация работы <highlighttext>преподавателей</highlighttext>, '
                                        'расписание занятий, поддержка в организационных вопросах. ')
def test_repr(test_getvacancy):
    for vacancy in test_getvacancy:
        assert repr(vacancy) == (f'({vacancy.name}\n, {vacancy.link}\n, {vacancy.salary_from}\n, {vacancy.salary_to}\n, {vacancy.currency}\n, {vacancy.responsibility}\n)')


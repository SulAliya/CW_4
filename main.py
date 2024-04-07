from src.get_vacancies import GetVacancy
from src.json_list import HeadHunterAPI
from src.add_vacancy import VacancyList


def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh_api = HeadHunterAPI()
    vacancies = hh_api.load_vacancies(search_query)
    list_of_vacancies = []
    for vacancy_parameters in vacancies['items']:
        if isinstance(vacancy_parameters, dict):
            name = vacancy_parameters.get('name')
            link = vacancy_parameters.get('alternate_url')
            salary = vacancy_parameters.get('salary')
            if salary:
                salary_from = salary.get('from', 'Зарплата не указана')
                salary_to = salary.get('to', 'не указано')
                currency = salary.get('currency')
            else:
                salary_from = 'Зарплата не указана'
                salary_to = ''
                currency = ''
            description = vacancy_parameters.get('snippet', )
            if description:
                responsibility = description.get('responsibility')
            else:
                responsibility = 'не указано'
            list_of_vacancies.append(GetVacancy(name, link, salary_from, salary_to, currency, responsibility))

    filtered_vacancies = list(filter(lambda s: s not in filter_words, list_of_vacancies))
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x.salary_from is not None, reverse=True)
    ranged_vacancies = sorted_vacancies[:top_n]
    for vacancy_parameters in ranged_vacancies[:top_n]:
        print(vacancy_parameters)
    save_json = VacancyList('data/hh_vacancies.json')
    save_json.save_vacancy(vacancies)


if __name__ == "__main__":
    user_interaction()

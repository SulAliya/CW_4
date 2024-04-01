from src.get_vacancies import GetVacancy
from src.json_list import HeadHunterAPI
from src.add_vacancy import VacancyList

def user_interaction():
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000

    hh_api = HeadHunterAPI()
    vacancies = hh_api.load_vacancies(search_query)
    # print(vacancies)

    if vacancies and 'items' in vacancies:
        list_of_vacancies = []
        for vacancy_parameters in vacancies['items']:
            if isinstance(vacancy_parameters, dict):
                name = vacancy_parameters.get('name')
                link = vacancy_parameters.get('alternate_url')
                salary = vacancy_parameters.get('salary')
                if salary:
                    salary_from = salary.get('from')
                else:
                    salary_from = 'Зарплата не указана'
                description = vacancy_parameters.get('snippet')
                list_of_vacancies.append({'Вакансия': name, 'Ссылка': link, 'Зарплата от': salary_from, 'Описание': description} )
            elif isinstance(vacancy_parameters, GetVacancy):
                list_of_vacancies.append(vacancy_parameters)
            print(list_of_vacancies)

    # filtered_vacancies = filter_vacancies(list_of_vacancies, filter_words)
    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()

class Vacancy:
    """
    Информация о вакансии
    """

    def __init__(self, vacancy_title, town, salary_from, salary_to, employment, url):
        self.vacancy_title: str = vacancy_title
        self.town: str = town
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.employment: str = employment
        self.url: str = url

    def __str__(self):
        return f'Название вакансии: {self.vacancy_title}\n' \
               f'Город: {self.town}\n' \
               f'Зарплата от: {self.salary_from}\n' \
               f'Зарплата до: {self.salary_to}\n' \
               f'Тип занятости: {self.employment}\n' \
               f'Ссылка на вакансию: {self.url}\n'

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from > other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError("Вакансию можно сравнивать только с вакансией")
        return self.salary_from >= other.salary_from

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            'vacancy_title': self.vacancy_title,
            'town': self.town,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'employment': self.employment,
            'url': self.url
        }

    @staticmethod
    def to_list_dict(vacancy_dict):
        """Возвращает вакансии в виде списка"""
        return Vacancy(
            vacancy_dict['vacancy_title'],
            vacancy_dict['town'],
            vacancy_dict['salary_from'],
            vacancy_dict['salary_to'],
            vacancy_dict['employment'],
            vacancy_dict['url']
        )


class Vacancies:
    """Обработка списка вакансий"""

    def __init__(self):
        self.__all_vacancies = []

    def add_vacancies(self, new_vacancies):
        self.__all_vacancies += new_vacancies

    def delete_vacancies(self, old_vacancies):
        for i in old_vacancies:
            self.__all_vacancies.remove(i)

    def sort_vacancies_by_salary(self):
        self.__all_vacancies.sort(reverse=True)

    @property
    def all_vacancies(self):
        return self.__all_vacancies

    def to_list_dict(self):
        total = []
        for i in self.__all_vacancies:
            total.append(i.to_dict())
        return total

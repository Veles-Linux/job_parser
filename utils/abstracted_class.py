from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """Абстрактный класс для получения вакансий"""

    @abstractmethod
    def get_vacancies(self, name_job, pages):
        pass


class SaverJSON(ABC):
    """
    Запись полученных вакансий в файл json и чтение
    """

    @abstractmethod
    def file_reader(self):
        pass

    @abstractmethod
    def file_writer(self):
        pass

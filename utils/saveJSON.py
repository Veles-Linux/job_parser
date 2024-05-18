import json
from utils.vacancies import Vacancy, Vacancies
from utils.abstracted_class import SaverJSON


class JSONSaver(Vacancies, SaverJSON):
    """
    Класс для записи и чтения JSON файла
    """

    def file_writer(self):
        """
        Запись файла
        """
        name_file = input('Назовите файл: ') + '.json'
        with open(name_file, 'w', encoding='utf-8') as file:
            json.dump(self.to_list_dict(), file, indent=4, ensure_ascii=False)

    def file_reader(self):
        """
        Чтение файла
        """
        with open('vacancies.json', 'r', encoding='UTF-8') as file:
            list_dict = json.load(file)
            self.all_vacancies = []
            for i in list_dict:
                self.all_vacancies.append(Vacancy.from_list_dict(i))

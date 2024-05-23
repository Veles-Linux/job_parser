from utils.api_hh import HeadHunterAPI
from utils.saveJSON import JSONSaver
from utils.api_sj import SuperJobAPI
import json


def user_choice_hh():
    """Функция для фильтра вакансий HH.ru"""
    keyword = input('Напишите название профессии: \n')
    hh_api = HeadHunterAPI()
    print('Сколько вывести страниц? \n')
    pages = int(input())
    from_hh = hh_api.get_vacancies(keyword, pages)
    print('Список вакансий с сайта "HeadHuter": \n')
    for i in from_hh:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Завершено')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()
        return jsonfile_hh


def user_choice_sj():
    """Функция для фильтра вакансий SuperJob"""
    keyword = input('Напишите название профессии: \n')
    superjob_api = SuperJobAPI()
    print('Сколько вывести страниц? \n')
    pages = int(input())
    from_sj = superjob_api.get_vacancies(keyword, pages)
    print('Список вакансий с сайта "SuperJob": \n')
    for i in from_sj:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Завершено')
    else:
        jsonfile_sj = JSONSaver()
        jsonfile_sj.add_vacancies(from_sj)
        jsonfile_sj.sort_vacancies_by_salary()
        jsonfile_sj.file_writer()
        return jsonfile_sj


def del_vacancy():
    """Функция для удаления вакансии по индексу"""
    file = open("Вакансии.json", 'r', encoding='UTF-8')
    file = json.load(file)
    del file[int(input())]
    file_new = open("Вакансии.json", "w", encoding='UTF-8')
    data = file
    json.dump(data, file_new, indent=4, ensure_ascii=False)

    return file

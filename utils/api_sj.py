import os
import requests
from utils.vacancies import Vacancy
from utils.abstracted_class import GetVacancies

SUPERJOB_API_KEY = 'v3.r.138358255.44d8fe800c164c4c6e7c2c345a03ba757ee5a78f.8da20465d0e22d776ba4c55a2cd32eaaae8098c9'


class SuperJobAPI(GetVacancies):
    """Класс для подключения к сайту SJ.ru"""
    def get_vacancies(self, name_job, pages):
        sj_list = []
        head = {'Host': 'api.superjob.ru',
                'X-Api-App-Id': SUPERJOB_API_KEY
                }

        for i in range(pages):
            params = {
                'keyword': name_job,
                'count': 5,
                'page': i
            }

            response = requests.get('https://api.superjob.ru/2.0/vacancies/', params=params, headers=head)
            status_sj = response.status_code
            if status_sj == 200:
                response_json = response.json()

                for j in response_json['objects']:
                    sj_title = j['profession']
                    if j['address'] is None:
                        sj_town = None
                    else:
                        sj_town = j['town']['title']
                    if not ((j['payment_from'] is None) or (j['payment_to'] is None)):
                        sj_salary_from = j['payment_from']
                        sj_salary_to = j['payment_to']
                    else:
                        sj_salary_from = 0
                        sj_salary_to = 0
                    sj_employment = j['type_of_work']['title']
                    sj_url = j['link']

                    sj_vacancy = Vacancy(sj_title, sj_town, sj_salary_from, sj_salary_to, sj_employment, sj_url)
                    sj_list.append(sj_vacancy)
            else:
                print(f'Код: {status_sj}')
            return sj_list

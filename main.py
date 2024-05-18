from utils.utils import user_choice_hh, user_choice_sj


def main():
    """Функция для взаимодействия с пользователем"""
    print('Здравствуйте! \n'
          'Эта программа поможет Вам в поиске вакансий на сайтах: HeadHunter и SuperJob. \n'
          'Введите цифру от 1 до 3: \n')

    while True:
        print('\n1 - HeadHunter \n'
              '2 - SuperJob \n'
              '3 - Закрыть программу. \n')

        user_choice_platform = input()
        if user_choice_platform == '1':
            print('HeadHunter')
            user_choice_hh()

        elif user_choice_platform == '2':
            print('SuperJob')
            user_choice_sj()

        elif user_choice_platform == '3':
            print('До свидания')
            break

        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    main()

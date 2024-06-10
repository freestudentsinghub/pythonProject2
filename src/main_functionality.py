from src.processing import filter_by_state
from src.utils import list_of_the_transaction
from src.processing import filter_by_state, sorted_by_datetime


def main_functionality():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями.\n "
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из json файла\n"
          "2. Получить информацию о транзакциях из csv файла\n"
          "3. Получить информацию о транзакциях из xlsx файла\n")
    number = int(input())
    if number == 1:
        print('Для обработки выбран json файл.')
        print('Введите статус по которому необходимо выполнить фильтрацию.\n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        while True:
            status = input().upper()
            if status in ['EXECUTED', 'CANCELED', 'PENDING']:
                list_status = filter_by_state(list_of_the_transaction(filename="../data/operations.json"), status)
                print('Отсортировать операции по дате? Да/Нет')

                user_answer = input()
                if user_answer == 'Да':
                    print('Отсортировать по возрастанию или по убыванию?')
                    user_answer_1 = input()
                    if user_answer_1 == 'по возрастанию':
                        sorted_data_true = sorted_by_datetime(list_status, 'ascending')
                        print('Выводить только рублевые тразакции? Да/Нет')
                        user_answer_3 = input()
                        if user_answer_3 == 'Да':
                            if sorted_data_true["operationAmount"]["currency"]["code"] == "RUB":
                                return sorted_data_true["operationAmount"]["amount"]

                    else:
                        sorted_data_false = sorted_by_datetime(list_status, "descending")
                        print('Выводить только рублевые тразакции? Да/Нет')
                        user_answer_2 = input()
                        return sorted_data_false
                else:
                    pass

            else:
                print(f'Статус операции "{status}" недоступен.')

    elif number == 2:
        print('Для обработки выбран csv файл.')

        print('Введите статус по которому необходимо выполнить фильтрацию.\n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        while True:
            status = input().upper()
            if status in ['EXECUTED', 'CANCELED', 'PENDING']:
                return status
            else:
                print(f'Статус операции "{status}" недоступен.')
    elif number == 3:
        print('Для обработки выбран xlsx файл.')

        print('Введите статус по которому необходимо выполнить фильтрацию.\n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        while True:
            status = input().upper()
            if status in ['EXECUTED', 'CANCELED', 'PENDING']:
                return status
            else:
                print(f'Статус операции "{status}" недоступен.')


print(main_functionality())

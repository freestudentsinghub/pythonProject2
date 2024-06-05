from src.processing import filter_by_state
from src.utils import list_of_the_transaction
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
                return list_status
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
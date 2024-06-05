from src.processing import sorted_by_datetime
from src.utils import list_of_the_transaction
from src.transactions_csv import read_csv
from src.transactions_excel import read_excel
def main():

    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями.\n "
          "Выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из json файла\n"
          "2. Получить информацию о транзакциях из csv файла\n"
          "3. Получить информацию о транзакциях из xlsx файла\n")
    user_input = int(input())

    if user_input == 1:
        data = list_of_the_transaction("../data/operations.json")
        print('Для обработки выбран json файл.')

    elif user_input == 2:
        data = read_csv("../data/operations.json")
        print('Для обработки выбран csv файл.')

    elif user_input == 3:
        data = read_excel("data/transactions_excel.xlsx")
        print('Для обработки выбран xlsx файл.')

    print('Введите статус по которому необходимо выполнить фильтрацию.\n'
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    status = input().upper()
    if status in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f'Операции отфильтрованы по статусу "{status}"')
    else:
        print(f'Статус операции "{status}" недоступен.')
        if status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу "{status}"')

    print('Отсортировать операции по дате? Да/Нет')
    user_input_data = input()
    print('Отсортировать по возрастанию или по убыванию?')
    user_input_tf = input()

    if user_input_data == 'Да' and user_input_tf == 'по убыванию':
        sorted_by_date = sorted_by_datetime(data, True)








print(main())


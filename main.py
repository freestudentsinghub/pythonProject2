from src.processing import filter_by_state, sorted_by_datetime
from src.re_transactions import transactions_re
from src.transactions_csv import read_csv
from src.transactions_excel import read_excel
from src.utils import list_of_the_transaction
from src.widget import mask_kard_and_mask_account


def main() -> None:
    """функциz main в модуле main, которая отвечает за основную логику проекта
    с пользователем и связывает функциональности между собой."""

    print(
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями.\n "
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из json файла\n"
        "2. Получить информацию о транзакциях из csv файла\n"
        "3. Получить информацию о транзакциях из xlsx файла\n"
    )
    user_input = int(input())

    if user_input == 1:
        data = list_of_the_transaction("data/operations.json")
        print("Для обработки выбран json файл.")

    elif user_input == 2:
        data = read_csv("data/transactions.csv")
        print("Для обработки выбран csv файл.")

    elif user_input == 3:
        data = read_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран xlsx файл.")

    print(
        "Введите статус по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    status = input().upper()
    while True:
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{status}"')
            list_transaction = filter_by_state(data, status)
            print("Отсортировать операции по дате? Да/Нет")
            user_input_data = input()

            if user_input_data == "Да":
                print("Отсортировать по возрастанию или по убыванию?")
                user_input_ascending = input()
                if user_input_ascending == "по возрастанию":
                    list_transaction = sorted_by_datetime(list_transaction, True)
                else:
                    list_transaction = sorted_by_datetime(list_transaction, False)

            print("Выводить только рублевые тразакции? Да/Нет")
            user_input_rub = input()
            if user_input_rub == "Да":
                list_currency = []

                for i in list_transaction:
                    if "currency_code" in i.keys():
                        if i["currency_code"] == "RUB":
                            list_currency.append(i)
                    else:
                        if i["operationAmount"]["currency"]["code"] == "RUB":
                            list_currency.append(i)
            else:
                list_currency = list_transaction
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            user_input_word = input()
            if user_input_word == "Да":
                list_currency = transactions_re(list_transaction, pattern="Перевод организации")

            print("Распечатываю итоговый список транзакций...")
            if len(list_currency) != 0:
                print(f"Всего банковских операций в выборке: {len(list_currency)}")
                for i in list_currency:
                    date = i["date"]
                    description = i["description"]
                    account_from = str(i.get("from", "without_from"))
                    account_to = i["to"]
                    if "amount" in i:
                        amount = i["amount"]
                    else:
                        amount = i["operationAmount"]["amount"]

                    print(
                        f"{date} {description}",
                        f"\n{mask_kard_and_mask_account(account_from)} -> {mask_kard_and_mask_account(account_to)}",
                        f"\nСумма: {amount} руб.\n",
                    )

            else:
                print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
            break
        else:
            print(f'Статус операции "{status}" недоступен.')


if __name__ == "__main__":
    main()

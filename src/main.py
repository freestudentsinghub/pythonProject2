from src.main_functionality import main_functionality
from src import utils
transactions = utils.list_of_the_transaction(filename="../data/operations.json")
def main():
    status = main_functionality()
    if status == 'CANCELED':
        canceled_transactions = []
        for i in transactions:
            if 'state' in i and i["state"] == 'CANCELED':
                canceled_transactions.append(i)
        return canceled_transactions
    elif status == "EXECUTED":
        executed_transactions = []
        for i in transactions:
            if 'state' in i and i['state'] == "EXECUTED":
                executed_transactions.append(i)
        return executed_transactions

print(main())







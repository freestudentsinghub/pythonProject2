from typing import List

from main import nwe_list

def amount_rub(nwe_list: List[dict]) -> List[dict]:
    rub_list = []
    for amount in nwe_list:
        if "operationAmount" in amount and "currency" in amount["operationAmount"] and amount["operationAmount"]["currency"]["code"] == "RUB":
            rub_list.append(amount["operationAmount"]["amount"])
    return rub_list

rub_a_l = amount_rub(nwe_list)
for amount in rub_a_l:
    print(amount)







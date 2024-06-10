from src.masks import mask_account, mask_card


def mask_kard_and_mask_account(name_card_and_name_account: str) -> str:
    """ "функция выводит маску на счет и номер карты"""
    if name_card_and_name_account.startswith("Счет"):
        mask_card_nwe = mask_account(name_card_and_name_account)
        return "Счет" + " " + "".join(mask_card_nwe)
    else:
        num = "".join([num for num in name_card_and_name_account if num.isdigit()])
        name = name_card_and_name_account.replace(num, "")
        mask_number = mask_card(num).strip()
        return f"{name} {''.join(mask_number)}"


def data_mask(data_number: str) -> str:
    """функция, которая принимает на вход строку,
    вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"""
    list_number = list(data_number)
    number_data = list_number[8:10] + ["."] + list_number[5:7] + ["."] + list_number[0:4]
    return "".join(number_data)


# print(mask_kard_and_mask_account("Счет 35383033474447895560"))
# print(mask_kard_and_mask_account("Maestro 1596837868705199"))
# print(data_mask("2018-07-11T02:26:18.671407"))
# print(mask_kard_and_mask_account("Visa Platinum 8990922113665229"))
# print(mask_kard_and_mask_account("Visa Gold 5999414228426353"))
# print(mask_kard_and_mask_account("Visa Classic 6831982476737658"))

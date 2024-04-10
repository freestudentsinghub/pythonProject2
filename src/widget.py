def mask_kard_and_cout(name_card_and_count: str) -> str:
    """ "функция выводит маску на счет и номер карты"""
    if name_card_and_count.startswith("Счет"):
        list_kard_number = list(name_card_and_count)
        mask_card = ["**"] + list_kard_number[-4:]
        return "".join(mask_card)
    else:
        list_number = list(name_card_and_count)
        mask_number = list_number[-16:-12] + [" "] + list_number[-12:-10] + ["** ****"] + [" "] + list_number[-4:]
        return "".join(mask_number)


def data_mask(data_number: str) -> str:
    """функция, которая принимает на вход строку,
    вида "2018-07-11T02:26:18.671407"
    и возвращает строку с датой в виде "11.07.2018"""
    list_number = list(data_number)
    number_data_return = list_number[8:10] + ["."] + list_number[5:7] + ["."] + list_number[0:4]
    return "".join(number_data_return)


print(mask_kard_and_cout("Счет 35383033474447895560"))
print(mask_kard_and_cout("Maestro 1596837868705199"))
print(data_mask("2018-07-11T02:26:18.671407"))

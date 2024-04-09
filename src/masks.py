def mask_card(kard_number: str) -> str:
    """Функция которая делает маску в середине номера карты"""

    list_number_card = list(kard_number)
    mask_kard = list_number_card[0:4] + [" "] + list_number_card[4:6] + ["** ****"] + [" "] + list_number_card[-4:]
    return "".join(mask_kard)


def mask_account(kard_number: str) -> str:
    """Функция которая делает маску из всех чисел кроме последних 4"""

    list_kard_number = list(kard_number)
    mask_card = ["**"] + list_kard_number[-4:]
    return "".join(mask_card)


print(mask_card("7000792289606361"))
print(mask_account("73654108430135874305"))

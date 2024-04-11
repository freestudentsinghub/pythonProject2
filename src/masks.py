def mask_card(card_number: str) -> str:
    """Функция которая делает маску в середине номера карты"""

    list_number_card = list(card_number)
    mask_card = list_number_card[0:4] + [" "] + list_number_card[4:6] + ["** ****"] + [" "] + list_number_card[-4:]
    return "".join(mask_card)


def mask_account(card_number: str) -> str:
    """Функция которая делает маску из всех чисел кроме последних 4"""

    list_card_number = list(card_number)
    mask_card = ["**"] + list_card_number[-4:]
    return "".join(mask_card)

def get_mask_kard(name_and_card: str) -> str:
    """ "функция выводит маску на счет и номер карты"""
    if name_and_card.startswith("Счет"):
        list_kard_number = list(name_and_card)

        mask_card = ["**"] + list_kard_number[-4:]
        return "".join(mask_card)
    else:
        list_number = list(name_and_card)
        mask_number = list_number[-16:-12] + [" "] + list_number[-12:-10] + ["** ****"] + [" "] + list_number[-4:]
        return "".join(mask_number)

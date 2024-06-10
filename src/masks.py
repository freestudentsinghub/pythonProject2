from src.logger import setup_logger

# вызов логера
logger = setup_logger("masks", "masks.log")


def mask_card(card_number: str) -> str:
    """Функция которая делает маску в середине номера карты"""
    logger.info(f"start mask_card {card_number}")

    list_number_card = list(card_number)
    mask_card = list_number_card[0:4] + [" "] + list_number_card[4:6] + ["** ****"] + [" "] + list_number_card[-4:]
    logger.info(f'mask {"".join(mask_card)}')
    return "".join(mask_card)


# print(mask_card("1234567890"))


def mask_account(card_number: str) -> str:
    """Функция которая делает маску из всех чисел кроме последних 4"""
    logger.info(f"start mask_account {card_number}")
    list_card_number = list(card_number)
    mask_card = ["**"] + list_card_number[-4:]
    logger.info(f'mask {"".join(mask_card)}')
    return "".join(mask_card)


# print(mask_account("12534567890"))

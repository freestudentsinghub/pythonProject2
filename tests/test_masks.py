from src import masks


def test_masks():
    """Проверяет функции из модуля masks"""
    assert masks.mask_card("7000792289606361") == "7000 79** **** 6361"
    assert masks.mask_account("73654108430135874305") == "**4305"

from utils.descriptors import (
    IntegerField,
    IDField,
    CharField,
    StateField,
    CurrencyNameField,
    CurrencyCodeField,
    DateField,
    AccountField,
    MoneyAmountField,
)

import pytest


def test_descriptors():
    class MyClass:
        integer_field = IntegerField()
        id_field = IDField()
        char_field = CharField()
        state_field = StateField()
        name_field = CurrencyNameField()
        code_field = CurrencyCodeField()
        date_field = DateField()
        acc_field = AccountField()
        money_field = MoneyAmountField()

    obj = MyClass()

    obj.integer_field = 10
    assert obj.integer_field == 10

    with pytest.raises(ValueError):
        obj.integer_field = "not an integer"

    obj.id_field = 1
    assert obj.id_field == 1

    with pytest.raises(ValueError):
        obj.id_field = 0

    with pytest.raises(ValueError):
        obj.id_field = -1

    obj.char_field = "char"
    assert obj.char_field == "char"

    with pytest.raises(ValueError):
        obj.char_field = {}

    obj.state_field = "EXECUTED"
    assert obj.state_field == "EXECUTED"

    obj.state_field = "CANCELED"
    assert obj.state_field == "CANCELED"

    with pytest.raises(ValueError):
        obj.state_field = "SOMESTATE"

    obj.name_field = "руб."
    assert obj.name_field == "руб."

    obj.name_field = "USD"
    assert obj.name_field == "USD"

    with pytest.raises(ValueError):
        obj.name_field = "wrong_name"

    obj.code_field = "RUB"
    assert obj.code_field == "RUB"

    obj.code_field = "USD"
    assert obj.code_field == "USD"

    with pytest.raises(ValueError):
        obj.code_field = "wrong_code"

    obj.date_field = "1994-12-05"
    assert obj.date_field == "05.12.1994"

    with pytest.raises(ValueError):
        obj.date_field = "1000/12/03"

    obj.acc_field = "Card1234123412341234"
    assert obj.acc_field == "Card 1234 12** **** 1234"

    obj.acc_field = "Счет12345123451234512345"
    assert obj.acc_field == "Счет **2345"

    with pytest.raises(ValueError):
        obj.acc_field = "Счет1"

    with pytest.raises(ValueError):
        obj.acc_field = "Сard 1234"

    obj.money_field = "0.20"
    assert obj.money_field == "0.20"

    with pytest.raises(ValueError):
        obj.money_field = "119.234"

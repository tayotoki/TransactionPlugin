from utils.descriptors import (
    IDField,
    CharField,
    StateField,
    DateField,
    AccountField,
    CurrencyField,
    MoneyAmountField,
)


class Operation:
    id = IDField()
    state = StateField()
    date = DateField()
    amount = MoneyAmountField()
    currency_name = CurrencyField()
    currency_code = CurrencyField()
    description = CharField()
    from_ = AccountField()
    to = AccountField()

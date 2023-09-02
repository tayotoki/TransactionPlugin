from utils.descriptors import (
    IDField,
    CharField,
    StateField,
    DateField,
    AccountField,
    CurrencyNameField,
    CurrencyCodeField,
    MoneyAmountField,
)


class Operation:
    id = IDField()
    state = StateField()
    date = DateField()
    amount = MoneyAmountField()
    currency_name = CurrencyNameField()
    currency_code = CurrencyCodeField()
    description = CharField()
    from_ = AccountField()
    to = AccountField()

    def __repr__(self):
        if self.from_:
            return f"{self.date} {self.description}\n" \
                   f"{self.from_} -> {self.to}\n" \
                   f"{self.amount} {self.currency_name}\n"

        return f"{self.date} {self.description}\n" \
               f"{self.to}\n" \
               f"{self.amount} {self.currency_name}\n"

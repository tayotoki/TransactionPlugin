import re
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any

from .functions import get_hidden_cart_number

STATE_CHOICES = (
    "EXECUTED",
    "CANCELED",
)

CURRENCY_CHOICES = {
    "codes": ["RUB", "USD"],
    "names": ["руб", "USD"],
}


class Field(ABC):
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        self.check_params(
            field_name=self.name,
            set_value=value
        )

        setattr(__obj=instance, __name=self.name, __value=value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    @classmethod
    @abstractmethod
    def check_params(cls, field_name: str, set_value: Any):
        pass


class IntegerField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if set_value.__class__ is not int:
            raise ValueError("Field must be an integer")


class IDField(IntegerField):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        super().check_params(field_name, set_value)

        if set_value < 0:
            raise ValueError("id field must be positive integer number")
        elif set_value == 0:
            raise ValueError("id can't be zero as primary key")


class CharField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if set_value.__class__ is not str:
            raise ValueError(f"Field must be a string type, got "
                             f"{set_value.__class__}")


class StateField(CharField):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        super().check_params(field_name, set_value)

        if set_value not in STATE_CHOICES:
            raise ValueError("Incorrect state for transaction")


class CurrencyField(CharField):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        super().check_params(field_name, set_value)

        if set_value not in CURRENCY_CHOICES["names"] or \
           set_value not in CURRENCY_CHOICES["codes"]:
            raise ValueError("Unknown code/name currency")


class DateField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        try:
            datetime.strptime(set_value, "%Y-%m-%d")
        except Exception as e:
            print(f"{e}"
                  f"Incorrect date for DateField")
            exit(1)

    def __get__(self, instance, owner):
        return getattr(instance, self.name).strftime("%d.%m.%Y")


class AccountField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if not re.fullmatch(r"[A-Za-z А-Яа-я]*(\d){16}", set_value):
            raise ValueError("Incorrect account data")

    def __get__(self, instance, owner):
        account_info: str = getattr(instance, self.name)

        return get_hidden_cart_number(account_info)


class MoneyAmountField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if not re.fullmatch(
            r"[^-]\d+[.]\d{2}",
            set_value
        ):
            raise ValueError("Incorrect money amount")



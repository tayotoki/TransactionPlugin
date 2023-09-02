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
    "names": ["руб.", "USD"],
}

NULLABLE_FIELDS = ["from"]


class Field(ABC):
    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    def __set__(self, instance, value):
        if value is not None:
            self.check_params(
                field_name=self.name,
                set_value=value
            )
        else:
            if self.name.strip("_") not in NULLABLE_FIELDS:
                raise ValueError(f"{self.name.strip('_')} field can't be None")

        setattr(instance, self.name, value)

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


class CurrencyNameField(CharField):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        super().check_params(field_name, set_value)

        if set_value.strip() not in CURRENCY_CHOICES["names"]:
            raise ValueError("Unknown name of currency")


class CurrencyCodeField(CharField):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        super().check_params(field_name, set_value)

        if set_value.strip() not in CURRENCY_CHOICES["codes"]:
            raise ValueError("Unknown code of currency")


class DateField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        try:
            datetime.strptime(set_value[:10], "%Y-%m-%d")
        except Exception as e:
            raise ValueError(f"{e}\n"
                             f"Incorrect date for DateField")

    def __get__(self, instance, owner):
        return datetime.strptime(
            getattr(instance, self.name)[:10],
            "%Y-%m-%d"
        ).strftime("%d.%m.%Y")


class AccountField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if "счет" not in set_value.lower():
            if re.fullmatch(r"[A-Za-z А-Яа-я]*\d{16}", set_value) is None:
                raise ValueError("Incorrect account data")
        else:
            if re.fullmatch(r"(Счет|счет) ?\d{20}", set_value) is None:
                raise ValueError("Incorrect account data")

    def __get__(self, instance, owner):
        account_info: str = getattr(instance, self.name)

        return get_hidden_cart_number(account_info)


class MoneyAmountField(Field):
    @classmethod
    def check_params(cls, field_name: str, set_value: Any):
        if set_value is not None:
            if not re.fullmatch(
                r"^[^-]?\d+[.]\d{2}$",
                set_value
            ):
                raise ValueError("Incorrect money amount")

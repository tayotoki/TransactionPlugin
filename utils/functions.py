import re


def get_hidden_cart_number(number: str):
    cart_name = re.search(
        r"(?P<cart_name>[A-Za-z А-Яа-я]*)(?= \d)",
        number,
    ).group("cart_info")

    cart_number: list[str] = re.findall(
        r"(?P<number>\d{4}){4}",
        number,
    )

    hidden_cart_number = " ".join([
        number if any(
            (i == 0,
             i == 4)
        ) else f"{number[:3]}**" if i == 2
        else "****"
        for i, number in
        enumerate(cart_number)
    ])

    return f"{cart_name} {hidden_cart_number}"

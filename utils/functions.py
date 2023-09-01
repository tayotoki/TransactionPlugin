import re


def get_hidden_cart_number(number: str) -> str:
    if number is None:
        return ""

    cart_name = re.search(
        r"(?P<cart_name>[A-Za-z А-Яа-я]*)(?= \d)",
        number,
    ).group("cart_name")

    if cart_name not in ("Счет", "счет"):
        cart_number: list[str] = re.findall(
            r"(?P<number>\d{4})",
            number,
        )

        hidden_cart_number: str = " ".join([
            number if any(
                (i == 0,
                 i == 3)
            ) else f"{number[:2]}**" if i == 1
            else "****"
            for i, number in
            enumerate(cart_number)
        ])

    else:
        cart_number: str = "".join(re.findall(
            r"(?P<number>\d{20})",
            number,
        ))

        hidden_cart_number = f"**{cart_number[-4:]}"

    return f"{cart_name} {hidden_cart_number}"

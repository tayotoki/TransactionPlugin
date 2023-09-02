from utils.functions import get_hidden_cart_number


def test_get_hidden_cart_number():
    first_case = None
    second_case = ""
    third_case = "Счет12345123451234512345"
    fourth_case = "Счет 12345123451234512345"
    fifth_case = "счет12345123451234512345"
    sixth_case = "счет 12345123451234512345"
    seventh_case = "VisaMaestroMasterGold 1234 1234 1234 1234"
    eighth_case = "Visa Maestro MasterGold 1234 1234 1234 1234"
    ninth_case = "Visa Maestro MasterGold 1234123412341234"

    assert get_hidden_cart_number(first_case) == ""
    assert get_hidden_cart_number(second_case) == ""
    assert get_hidden_cart_number(third_case) == "Счет **2345"
    assert get_hidden_cart_number(fourth_case) == "Счет **2345"
    assert get_hidden_cart_number(fifth_case) == "Счет **2345"
    assert get_hidden_cart_number(sixth_case) == "Счет **2345"
    assert get_hidden_cart_number(seventh_case) == "VisaMaestroMasterGold" \
                                                   " 1234 12** **** 1234"
    assert get_hidden_cart_number(eighth_case) == "Visa Maestro MasterGold" \
                                                  " 1234 12** **** 1234"
    assert get_hidden_cart_number(ninth_case) == "Visa Maestro MasterGold" \
                                                 " 1234 12** **** 1234"
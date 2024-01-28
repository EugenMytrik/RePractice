import re


def validate_phone_number(phone_number):
    pattern = r"^\d{10}$"
    return bool(re.match(pattern, phone_number))


valid_phone = "1234567890"
invalid_phone = "123-456-7890"
assert validate_phone_number(valid_phone) is True
assert validate_phone_number(invalid_phone) is False

import re


def validate_date_format(date):
    pattern = r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$"
    return bool(re.match(pattern, date))


valid_date = "12/31/2022"
invalid_date = "2022/12/31"
assert validate_date_format(valid_date) is True
assert validate_date_format(invalid_date) is False

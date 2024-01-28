import re


def extract_name_domain_from_email(email):
    pattern = r"(?P<name>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+\.[A-Z|a-z]{2,})"
    match = re.match(pattern, email)
    if match:
        return match.group("name"), match.group("domain")
    else:
        return None, None


sample_email = "john.doe@example.com"
assert extract_name_domain_from_email(sample_email) == ("john.doe", "example.com")

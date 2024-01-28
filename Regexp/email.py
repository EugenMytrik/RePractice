import re


def find_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(pattern, text)


text_with_emails = (
    "My email addresses are john.doe@example.com and alice_smith@gmail.com."
)
assert find_emails(text_with_emails) == [
    "john.doe@example.com",
    "alice_smith@gmail.com",
]

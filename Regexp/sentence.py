import re


def split_text_with_punctuation(text):
    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|!|\?)\s"
    return re.split(pattern, text)


sample_text = "This is sentence one. This is sentence two? And here is sentence three!"
assert split_text_with_punctuation(sample_text) == [
    "This is sentence one.",
    "This is sentence two?",
    "And here is sentence three!",
]

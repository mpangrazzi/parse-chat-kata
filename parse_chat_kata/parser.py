import re

DATE_REGEX = r"\d{2}:\d{2}:\d{2}"
NAME_REGEX = r"\w+\s(\s?\w+\s?(?=:))?:?\s?"
DATE_NAME_REGEX = re.compile(r"^(%s) (%s)" % (DATE_REGEX, NAME_REGEX))

global customer_name


def parse(text: str):
    return [parse_sentence(i, sent) for i, sent in enumerate(get_sentences(text))]


def get_sentences(text: str):
    sents = (
        text.splitlines(True)
        if re.search("\n+", text)
        else re.split(r"(?=%s \w+)" % DATE_REGEX, text)
    )

    return filter(None, sents)


def parse_sentence(i: int, sent: str):
    global customer_name

    match = DATE_NAME_REGEX.match(sent)
    date, name, _ = match.groups()

    if i == 0:
        customer_name = name

    return {
        "date": date,
        "mention": f"{date} {name}",
        "sentence": sent[match.span()[1] :],
        "type": "customer" if name == customer_name else "agent",
    }

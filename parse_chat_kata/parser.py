import re

DATE_REGEX = r"\d{2}:\d{2}:\d{2}"
NAME_REGEX = r"\w+"
DATE_NAME_REGEX = re.compile(r"(%s) (%s :?\s?)" % (DATE_REGEX, NAME_REGEX))


def parse(text: str):
    return [parse_sentence(sent) for sent in get_sentences(text) if sent]


def get_sentences(text: str):
    return (
        text.splitlines(True)
        if re.search("\n+", text)
        else re.split(r"(?=%s %s :?)" % (DATE_REGEX, NAME_REGEX), text)
    )


def parse_sentence(sent: str):
    match = DATE_NAME_REGEX.match(sent)

    date, name = match.groups()
    sep = match.span()[1]
    sentence = sent[sep:]

    return {
        "date": date,
        "mention": f"{date} {name}",
        "sentence": sentence,
        "type": "customer" if "Customer" in name else "agent",
    }

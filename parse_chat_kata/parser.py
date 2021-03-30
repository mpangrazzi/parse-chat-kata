import re


def parse(text: str):
    return [parse_sentence(sent) for sent in text.splitlines(True)]


def parse_sentence(text: str):
    match = re.match(r"(\d{2}:\d{2}:\d{2}) (.*?: )", text)

    date, name = match.groups()
    sep = match.span()[1]
    sentence = text[sep:]

    return {
        "date": date,
        "mention": f"{date} {name}",
        "sentence": sentence,
        "type": "customer" if "Customer" in name else "agent",
    }

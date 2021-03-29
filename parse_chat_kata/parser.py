import re


def parser(text: str):
    print(text)

    match = re.match("(?P<date>\d{2}:\d{2}:\d{2}) (?P<name>.*?: )", text)

    date, name = match.groups()
    sep = match.span()[1]
    sentence = text[sep:]

    sentences = []

    sentences.append(
        {
            "date": date,
            "mention": f"{date} {name}",
            "sentence": sentence,
            "type": "customer",
        }
    )

    return sentences

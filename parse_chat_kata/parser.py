import re


def parser(text: str):
    match = re.match(r"(\d{2}:\d{2}:\d{2}) (.*?: )", text)

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

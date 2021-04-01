from parse_chat_kata.parser import parse


def test_parse_single_sentence():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    )

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        }
    ]


def test_parse_single_sentence_with_surname():
    text = "14:24:32 Customer Service : Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer Service : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        }
    ]


def test_parse_multiple_sentences():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
        "14:26:15 Agent : Aliquam non cursus erat, ut blandit lectus."
    )

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n",
            "type": "customer",
        },
        {
            "date": "14:26:15",
            "mention": "14:26:15 Agent : ",
            "sentence": "Aliquam non cursus erat, ut blandit lectus.",
            "type": "agent",
        },
    ]


def test_full_chat():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
        "14:26:15 Agent : Aliquam non cursus erat, ut blandit lectus.\n"
        "14:27:00 Customer : Pellentesque cursus maximus felis, pharetra porta purus aliquet viverra.\n"
        "14:27:47 Agent : Vestibulum tempor diam eu leo molestie eleifend."
    )

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n",
            "type": "customer",
        },
        {
            "date": "14:26:15",
            "mention": "14:26:15 Agent : ",
            "sentence": "Aliquam non cursus erat, ut blandit lectus.\n",
            "type": "agent",
        },
        {
            "date": "14:27:00",
            "mention": "14:27:00 Customer : ",
            "sentence": "Pellentesque cursus maximus felis, pharetra porta purus aliquet viverra.\n",
            "type": "customer",
        },
        {
            "date": "14:27:47",
            "mention": "14:27:47 Agent : ",
            "sentence": "Vestibulum tempor diam eu leo molestie eleifend.",
            "type": "agent",
        },
    ]


def test_two_customer_mentions_as_start():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
        "14:27:00 Customer : Pellentesque cursus maximus felis, pharetra porta purus aliquet viverra.\n"
        "14:27:47 Agent : Vestibulum tempor diam eu leo molestie eleifend."
    )

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n",
            "type": "customer",
        },
        {
            "date": "14:27:00",
            "mention": "14:27:00 Customer : ",
            "sentence": "Pellentesque cursus maximus felis, pharetra porta purus aliquet viverra.\n",
            "type": "customer",
        },
        {
            "date": "14:27:47",
            "mention": "14:27:47 Agent : ",
            "sentence": "Vestibulum tempor diam eu leo molestie eleifend.",
            "type": "agent",
        },
    ]


def test_date_splitting():
    text = "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.14:26:15 Agent : Aliquam non cursus erat, ut blandit lectus."

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        },
        {
            "date": "14:26:15",
            "mention": "14:26:15 Agent : ",
            "sentence": "Aliquam non cursus erat, ut blandit lectus.",
            "type": "agent",
        },
    ]


def test_ignore_extra_dates():
    text = "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.14:26:15 Agent : I received it at 12:24:48, ut blandit lectus."

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        },
        {
            "date": "14:26:15",
            "mention": "14:26:15 Agent : ",
            "sentence": "I received it at 12:24:48, ut blandit lectus.",
            "type": "agent",
        },
    ]


def test_missing_colon_after_the_names():
    text = "14:24:32 Customer Lorem ipsum dolor sit amet, consectetur adipiscing elit.14:26:15 Agent I received it at 12:24:48, ut blandit lectus."

    sentences = parse(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        },
        {
            "date": "14:26:15",
            "mention": "14:26:15 Agent ",
            "sentence": "I received it at 12:24:48, ut blandit lectus.",
            "type": "agent",
        },
    ]

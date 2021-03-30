from os.path import join
from parse_chat_kata.parser import parser


def test_parse_single_sentence():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    )

    sentences = parser(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        }
    ]


def test_parse_multiple_sentences():
    text = (
        "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
        "14:26:15 Agent : Aliquam non cursus erat, ut blandit lectus."
    )

    sentences = parser(text)

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

    sentences = parser(text)

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

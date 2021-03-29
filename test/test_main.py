from parse_chat_kata.parser import parser


def test_parse_single_sentence():
    text = "14:24:32 Customer : Lorem ipsum dolor sit amet, consectetur adipiscing elit."

    sentences = parser(text)

    assert sentences == [
        {
            "date": "14:24:32",
            "mention": "14:24:32 Customer : ",
            "sentence": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "type": "customer",
        }
    ]

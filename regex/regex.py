def read_input() -> str:
    return input()


def question_mark(regex: str, text: str):
    # Preceding char occurs zero times
    if regex[0] != text[0]:
        return search(regex[2:], text)
    pass


def asterisk():
    pass


def plus():
    pass


def match(regex: str, text: str):
    if not regex:
        return True

    if regex == '$' and not text:
        return True

    if not regex[0] == text[0] and regex[0] != '.':
        return False

    return match(regex[1:], text[1:])


def search(regex: str, text: str):
    if not regex:
        return True

    if not text:
        return False

    if regex[0] == '^':
        return match(regex[1:], text)

    if match(regex, text):
        return True

    return search(regex, text[1:])


def main():
    usrinput = read_input()
    regex = usrinput.split('|')[0]
    text = usrinput.split('|')[-1]
    print(search(regex, text))


def testing():
    reg = 'colou?r'
    txt = 'color'
    print(search(reg, txt))


if __name__ == '__main__':
    testing()

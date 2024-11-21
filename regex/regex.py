def read_input() -> str:
    return input()


def match(regex: str, text: str):
    if not regex:
        return True

    elif regex == '$' and not text:
        return True

    elif not regex[0] == text[0] and regex[0] != '.':
        return False
    return match(regex[1:], text[1:])


def search(regex: str, text: str):
    if not regex:
        return True

    if regex[0] == '^':
        return match(regex[1:], text)

    if not text:
        return False

    elif match(regex, text):
        return True

    return search(regex, text[1:])


def main():
    usrinput = read_input()
    regex = usrinput.split('|')[0]
    text = usrinput.split('|')[-1]
    print(search(regex, text))


def testing():
    reg = '^apple$'
    txt = 'tasty apple'
    print(search(reg, txt))


if __name__ == '__main__':
    main()

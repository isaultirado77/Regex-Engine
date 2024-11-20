def read_input() -> str:
    return input()


def match(regex: str, text: str):
    if not regex:
        return True
    elif not text:
        return False
    elif not regex[0] == text[0] and regex[0] != '.':
        return False
    return match(regex[1:], text[1:])


def search(regex: str, text: str):
    pass


def find_flag(text: str, flag: str) -> list:
    return list(filter(lambda i: text[i] == flag, range(len(text))))


def dot(regex: str, string: str) -> bool:
    indexes = find_flag(string, '.')

    for index in indexes:
        if string[index] != regex[index]:
            return False

    return True


def main():
    usrinput = read_input()
    regex = usrinput.split('|')[0]
    text = usrinput.split('|')[-1]
    print(match(regex, text))


if __name__ == '__main__':
    main()

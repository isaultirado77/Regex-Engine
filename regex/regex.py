def read_input() -> str:
    return input()


def match(regex: str, string: str):
    if not regex:
        return True
    elif not string or regex[0] not in ('.', '', string[0]):
        return False
    return match(regex[1:], string[1:])


def find_flag(string: str, flag: str) -> list:
    return list(filter(lambda i: string[i] == flag, range(len(string))))


def dot(regex: str, string: str) -> bool:
    indexes = find_flag(string, '.')

    for index in indexes:
        if string[index] != regex[index]:
            return False

    return True


def main():
    usrinput = read_input()
    regex = usrinput.split('|')[0]
    string = usrinput.split('|')[-1]
    print(match(regex, string))


if __name__ == '__main__':
    main()

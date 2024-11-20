def read_input() -> str:
    return input()


def match(regex: str, string: str) -> bool:
    if len(regex) != len(string):
        return False

    if not regex:
        return True
    elif not string:
        return True if not regex else False
    elif '.' in regex:
        return dot(regex, string)
    else:
        return regex == string


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

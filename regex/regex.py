def read_input() -> str:
    return input()


def match(regex: str, string: str) -> bool:
    if not regex:
        return True
    elif not string:
        return True if not regex else False
    elif '.' in regex:
        return False
    else:
        return False


def main():
    regex = read_input()
    string = read_input()
    print(match(regex, string))


if __name__ == '__main__':
    main()

def read_input() -> str:
    return input()


def match(regex: str, string: str) -> bool:
    if not regex:
        return True
    elif not string:
        return True if not regex else False
    elif '.' in regex:
        return False  # Need to implement
    else:
        return False


def find_flag(string: str, flag: str) -> list:
    lst = list()
    for i in range(len(string)):
        if string[i] == flag:
            lst.append(i)
    return lst


def dot(regex: str, string: str):
    if len(regex) != len(string):
        return None

    indexes = find_flag(string, '.')
    pass


def main():
    regex = read_input()
    string = read_input()
    print(match(regex, string))


if __name__ == '__main__':
    s = '....cok.'

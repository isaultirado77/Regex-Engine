def read_input() -> str:
    return input()


def question_mark(regex: str, text: str):
    # Preceding char occurs zero or one time
    if len(regex) < 2:
        return False
    if regex[0] == text[0]:
        # Match first character and recurse with the rest
        return match(regex[2:], text[1:])
    else:
        # Proceed with the rest of the regex (zero occurrences)
        return match(regex[2:], text)


def asterisk(regex: str, text: str):
    if len(regex) < 2:
        return False
    if regex[0] == text[0]:
        return match(regex[2:], text[1:]) or asterisk(regex, text[1:])
    else:
        return match(regex[2:], text)


def plus(regex: str, text: str):
    if len(regex) > 2:
        return False


def match(regex: str, text: str):
    # Base case: if the regex is empty, we check if the text is empty as well
    if not regex:
        return not text

    if regex[0] == '^':  # Match the start of the string
        return match(regex[1:], text)

    if regex[0] == '$':
        return not text

    if len(text) == 0:  # If the text is empty and regex isn't, we can't match
        return False

    if regex[0] == text[0] or regex[0] == '.':  # Direct match or wildcard
        return match(regex[1:], text[1:])

    # Question-mark operator
    if len(regex) > 1 and regex[1] == '?':
        return question_mark(regex, text)

    # Asterisk operator
    if len(regex) > 1 and regex[1] == '*':
        return asterisk(regex, text)

    # Plus operator
    if len(regex) > 1 and regex[1] == '+':
        return plus(regex, text)


def search(regex: str, text: str):
    if not text:  # Base case: if text is empty, no match is possible
        return match(regex, text)

    if match(regex, text):
        return True
    return search(regex, text[1:])  # Try to match the regex from the next character of text


def main():
    usrinput = read_input()
    regex = usrinput.split('|')[0]
    text = usrinput.split('|')[-1]
    print(search(regex, text))


def testing():
    reg = 'colou*r'
    txt = 'color'
    print(search(reg, txt))


if __name__ == '__main__':
    testing()

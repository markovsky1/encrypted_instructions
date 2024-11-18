import sys


def decode_string(cipher: str) -> str:
    """Decrypts the compressed command string for the rover.

    Compressed string format:
        - The number before the square brackets indicates how many times the
        command must be repeated in parentheses.
        - Commands can contain nested brackets.
    """
    stack: list[tuple[str, int]] = []
    current_str: str = ''
    current_num: str = ''
    NUMBERS = '0123456789'

    for symbol in cipher:
        if symbol in NUMBERS:
            current_num += symbol
        elif symbol == '[':
            stack.append((current_str, int(current_num)))
            current_str, current_num = '', ''
        elif symbol == ']':
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += symbol

    return current_str


if __name__ == '__main__':
    input_str = sys.stdin.readline().rstrip()
    print(decode_string(input_str))

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE = len(ALPHABET)


def encode(num: int) -> str:
    if num == 0:
        return ALPHABET[0]

    digits = []
    while num > 0:
        num, remainder = divmod(num, BASE)
        digits.append(ALPHABET[remainder])

    return "".join(reversed(digits))


def decode(short_code: str) -> int:
    num = 0
    for char in short_code:
        num = num * BASE + ALPHABET.index(char)
    return num
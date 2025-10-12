def whole_string_to_base(string, base):
    num = int.from_bytes(string.encode("utf-8"), byteorder="big")
    digits = []

    while num > 0:
        digits.append(str(num % base))
        num //= base
    return ''.join(reversed(digits))


s = "AB"
result = whole_string_to_base(s, 16)
print(result)


def num_to_base(num, base) -> str:
    if num == 0:
        return "0"
    sign = "-" if num < 0 else ""
    num = abs(num)
    digits = ""
    while num > 0:
        digits = str(num % base) + digits
        num //= base
    return sign + digits


print(num_to_base(-7, 7))


"""
 while num > 0:
        digits.append(str(num % base))
        num //= base
"""
"""This is the main logic that converts it"""

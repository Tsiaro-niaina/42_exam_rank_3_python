"""
Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive.
Use digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs.
"""
def number_base_converter(
    number: str,
    from_base: int,
    to_base: int
) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"

    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    decimal_value = 0

    for char in number.upper():
        if char not in chars[:from_base]:
            return "ERROR"

        decimal_value = decimal_value * from_base + chars.index(char)

    if decimal_value == 0:
        return "0"

    result: list[str] = []

    while decimal_value:
        result.append(chars[decimal_value % to_base])
        decimal_value //= to_base

    return "".join(reversed(result))


if __name__ == "__main__":
    test_number = "1A"
    from_base = 16
    to_base = 10
    converted_number = number_base_converter(test_number, from_base, to_base)
    print(f"Number '{test_number}' in base {from_base} is '{converted_number}' in base {to_base}.")

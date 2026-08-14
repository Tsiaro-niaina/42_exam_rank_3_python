"""
Write a function that converts a number from one base to another.
Support bases from 2 to 36 inclusive.
Use digits 0-9 and letters A-Z for values 10-35.
Return "ERROR" for invalid inputs.
"""
def number_base_converter(number: str, from_base: int, to_base:int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"

    try:
        decimal_value = int(number, from_base)
    except ValueError:
        return "ERROR"

    if decimal_value == 0:
        return "0"

    digits = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        decimal_value //= to_base

    return ''.join(reversed(digits))


if __name__ == "__main__":
    test_number = "1A"
    from_base = 16
    to_base = 10
    converted_number = number_base_converter(test_number, from_base, to_base)
    print(f"Number '{test_number}' in base {from_base} is '{converted_number}' in base {to_base}.")

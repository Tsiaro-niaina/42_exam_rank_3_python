"""
Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again)
"""
def string_sculptor(text: str) -> str:
    to_low = True
    res = ""

    for char in text:
        if char.isspace():
            to_low = True
            res += char
        elif char.isalpha():
            if to_low:
                res += char.lower()
                to_low = False
            else:
                res += char.upper()
                to_low = True
        else:
            res += char

    return res


if __name__ == "__main__":
    test_string = "Hello World! This is a Test."
    print(f"Transformed string: '{string_sculptor(test_string)}'")

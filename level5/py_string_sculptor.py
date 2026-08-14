"""
Write a function that transforms a string by alternating the case of
alphabetic characters only.
Non-alphabetic characters remain unchanged and are NOT counted in the
alternation index.
The first alphabetic character should be lowercase, the second uppercase, etc.
Spaces reset the alternation (next alpha after a space is lowercase again)
"""
def string_sculptor(text: str) -> str:
    result = []
    lower = True

    for char in text:
        if char.isalpha():
            if lower:
                result.append(char.lower())
            else:
                result.append(char.upper())
            lower = not lower
        else:
            result.append(char)
            if char.isspace():
                lower = True

    return ''.join(result)


if __name__ == "__main__":
    test_string = "Hello World! This is a Test."
    print(f"Transformed string: '{string_sculptor(test_string)}'")

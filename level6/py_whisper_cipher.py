"""
Write a function that creates a Caesar cipher by shifting letters in a
string by a given amount.
Non-alphabetic characters should remain unchanged.
The shift can be negative (shift left).
"""
def whisper_cipher(text: str, shift: int) -> str:
    res: str = ""

    for c in text:
        if 'a' <= c <= 'z':
            res += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            res += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
        else:
            res += c

    return res


if __name__ == "__main__":
    test_string = "Hello, World!"
    shift_value = 3
    encrypted_string = whisper_cipher(test_string, shift_value)
    print(f"Original string: '{test_string}'")
    print(f"Encrypted string with shift {shift_value}: '{encrypted_string}'")

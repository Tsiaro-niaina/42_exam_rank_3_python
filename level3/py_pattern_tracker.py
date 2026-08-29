"""
Write a function that counts the number of valid consecutive digit pairs
in a string. A valid pair consists of two adjacent digits where the second
digit is exactly one greater than the first.
A 9 followed by a 0 is NOT a valid pair.
"""
def pattern_tracker(text: str) -> int:
    count = 0

    for a, b in zip(text, text[1:]):
        if '0' <= a <= '9' and '0' <= b <= '9':
            if int(b) == int(a) + 1:
                count += 1

    return count


if __name__ == "__main__":
    test_string = "12345678901234567890"
    print(f"Number of valid consecutive digit pairs in '{test_string}': {pattern_tracker(test_string)}")

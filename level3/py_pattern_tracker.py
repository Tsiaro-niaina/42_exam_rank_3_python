"""
Write a function that counts the number of valid consecutive digit pairs
in a string. A valid pair consists of two adjacent digits where the second
digit is exactly one greater than the first.
A 9 followed by a 0 is NOT a valid pair.
"""
def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) == int(text[i]) + 1:
                if not (text[i] == '9' and text[i + 1] == '0'):
                    count += 1
    return count


if __name__ == "__main__":
    test_string = "12345678901234567890"
    print(f"Number of valid consecutive digit pairs in '{test_string}': {pattern_tracker(test_string)}")

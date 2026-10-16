"""
Write a function that checks if a string is a palindrome,
ignoring spaces and case, only consider alphabetic characters
for the comparison.
A palindrome is a string that reads the same forwards and backwards.
"""
def echo_validator(text: str) -> bool:
    if not text:
        return False
    cleaned_text = ''.join(char.lower() for char in text if char.isalpha())
    return cleaned_text == cleaned_text[::-1]


if __name__ == "__main__":
    test_string = "A man a plan a canal Panama"
    print(f"Is the string '{test_string}' a palindrome? {echo_validator(test_string)}")

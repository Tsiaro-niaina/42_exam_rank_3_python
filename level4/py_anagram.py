"""
Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.
"""
def anagram(s1: str, s2: str) -> bool:
    cleaned_s1 = ''.join(char.lower() for char in s1 if char.isalpha())
    cleaned_s2 = ''.join(char.lower() for char in s2 if char.isalpha())
    return sorted(cleaned_s1) == sorted(cleaned_s2)


if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    print(f"Are '{string1}' and '{string2}' anagrams? {anagram(string1, string2)}")

"""
Write a function that checks if two strings are anagrams.
They must contain exactly the same letters with the same quantity,
ignoring case and spaces.
"""
def anagram(s1: str, s2: str) -> bool:
    count1: dict[str, int] = {}
    count2: dict[str, int] = {}

    for char in s1.lower():
        if char.isalpha():
            count1[char] = count1.get(char, 0) + 1

    for char in s2.lower():
        if char.isalpha():
            count2[char] = count2.get(char, 0) + 1

    return count1 == count2


if __name__ == "__main__":
    string1 = "Listen"
    string2 = "Silent"
    print(f"Are '{string1}' and '{string2}' anagrams? {anagram(string1, string2)}")

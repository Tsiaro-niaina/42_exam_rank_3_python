"""
Write a function that determines if two strings are permutations of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.
"""
def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


if __name__ == "__main__":
    string1 = "abcde"
    string2 = "edcba"
    print(f"Are '{string1}' and '{string2}' permutations of each other? {string_permutation_checker(string1, string2)}")

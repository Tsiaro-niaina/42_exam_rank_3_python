"""
Write a function that determines if two strings are permutations of each other.
Case sensitive. Whitespace and punctuation count as regular characters.
Empty strings are permutations of each other.
"""
def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    count: dict[str, int] = {}

    for char in s1:
        count[char] = count.get(char, 0) + 1

    for char in s2:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] == 0:
            del count[char]

    return not count

if __name__ == "__main__":
    string1 = "abcde"
    string2 = "edcba"
    print(f"Are '{string1}' and '{string2}' permutations of each other? {string_permutation_checker(string1, string2)}")

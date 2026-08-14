"""
Write a function that returns a string with the characters that appear
in both strings, without repetitions. Characters are added in the order
they appear in the first string.
"""
def inter(s1: str, s2: str) -> str:
    seen = set()
    result = []
    for char in s1:
        if char in s2 and char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result)


if __name__ == "__main__":
    string1 = "padinton"
    string2 = "paqefwtdjetyiytjneytjoeyjnejeyj"
    print(f"Common characters in '{string1}' and '{string2}': {inter(string1, string2)}")
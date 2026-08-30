"""
Write a function that sorts a list of strings according to multiple criteria:
1. Primary sort: By string length (shortest first)
2. Secondary sort: ASCII order, except letters are compared case-insensitively
   (for strings of same length)
3. Tertiary sort: By number of vowels (ascending, for same length and lexically equal)
4. Equal strings will appear in the same order as in the input list.
Forbidden functions: sorted(), list.sort()
"""
def cryptic_sorter(strings: list[str]) -> list[str]:

    def key(s: str) -> tuple[int, str, int]:
        vowels = sum(1 for c in s.lower() if c in 'aeiou')
        return (len(s), s.lower(), vowels)

    result = strings.copy()

    for i in range(1, len(result)):
        current = result[i]
        current_key = key(current)
        j = i - 1

        while j >= 0 and key(result[j]) > current_key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = current

    return result


if __name__ == "__main__":
    test_strings = ["aaa","bbb","AAA","BBB"]
    sorted_strings = cryptic_sorter(test_strings)
    print(f"Sorted strings based on ASCII sum: {sorted_strings}")

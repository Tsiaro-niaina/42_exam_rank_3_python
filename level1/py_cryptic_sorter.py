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
    def vowel_count(s: str) -> int:
        return sum(1 for char in s.lower() if char in 'aeiou')

    n = len(strings)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(strings[j]) > len(strings[j+1]):
                strings[j], strings[j+1] = strings[j+1], strings[j]
            elif len(strings[j]) == len(strings[j+1]):
                if strings[j].lower() > strings[j+1].lower():
                    strings[j], strings[j+1] = strings[j+1], strings[j]
                elif strings[j].lower() == strings[j+1].lower():
                    if vowel_count(strings[j]) > vowel_count(strings[j+1]):
                        strings[j], strings[j+1] = strings[j+1], strings[j]

    return strings
    

if __name__ == "__main__":
    test_strings = ["aaa","bbb","AAA","BBB"]
    sorted_strings = cryptic_sorter(test_strings)
    print(f"Sorted strings based on ASCII sum: {sorted_strings}")
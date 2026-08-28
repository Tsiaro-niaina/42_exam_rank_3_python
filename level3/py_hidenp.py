"""
Write a function that checks if the string 'small' is a subsequence
of 'big'. A subsequence means all characters of 'small' appear in 'big'
in the same order, but not necessarily consecutively.
Function is case-sensitive.
"""
def hidenp(small: str, big: str) -> bool:
    index = 0

    for char in big:
        if index < len(small) and char == small[index]:
            index += 1

    return index == len(small)


if __name__ == "__main__":
    small_string = "abc"
    big_string = "a1b2c3"
    print(f"Is '{small_string}' a subsequence of '{big_string}'? {hidenp(small_string, big_string)}")
